import time


class RateLimiter:
    def __init__(self, maxBucketSize, tokenRefillRate, refillRateInSeconds):
        self.maxBucketSize = maxBucketSize
        self.currentBucketSize = maxBucketSize
        self.refillRate = tokenRefillRate
        self.refillRateInSeconds = refillRateInSeconds
        self.lastRefreshedAt = time.time_ns()

    def requestHandler(self, requestId):
        self.checkRefill()
        print(
            "RequestId: {}, currentBucketSize: {}".format(
                requestId, self.currentBucketSize
            )
        )
        if self.currentBucketSize > 0:
            self.currentBucketSize -= 1
            print(f"Request {requestId} Processed")
            return True

        print(f"Request {requestId} blocked")
        return False

    def checkRefill(self):
        now = time.time_ns()
        timePassed = int((now - self.lastRefreshedAt) // 1e9)
        if timePassed == self.refillRateInSeconds:
            self.currentBucketSize = min(
                self.currentBucketSize + self.refillRate, self.maxBucketSize
            )
            self.lastRefreshedAt = now


# 5 request to be allowed per second
rateLimiter = RateLimiter(5, 5, 1)
for i in range(1, 20):
    rateLimiter.requestHandler(i)
    # Every request take 100 ms
    time.sleep(0.1)

# For concurrency handling
# - Either use a thread safe data structure
# - Or use synchronisation and Locks
# - Or Use Redis to store these values for quick access
