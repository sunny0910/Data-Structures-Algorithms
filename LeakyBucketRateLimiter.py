import threading, time
from collections import deque


class LeakyBucket:
    queue = deque()

    def __init__(self, maxBucketSize):
        self.maxBucketSize = maxBucketSize

    def reqestHandler(self, requestId):
        if len(self.queue) < self.maxBucketSize:
            self.queue.append(requestId)
            print(f"Request {requestId} processed")
            return True

        print(f"Request {requestId} blocked")
        return False

    @staticmethod
    def queueHandler():
        while True:
            # print("Reading Queue with length: ", len(LeakyBucket.queue))
            if LeakyBucket.queue:
                requestId = LeakyBucket.queue.popleft()
                print("request removed from queue")
            time.sleep(0.5)


threading.Thread(target=LeakyBucket.queueHandler, daemon=True).start()

ratelimiter = LeakyBucket(10)
for i in range(1, 20):
    print(f"Processing Request {i}")
    ratelimiter.reqestHandler(i)
    time.sleep(0.1)
