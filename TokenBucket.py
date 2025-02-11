import time
from abc import ABC, abstractmethod

class RateLimiter(ABC):
    @abstractmethod
    def requestHandler(self, requestId, tokens=None):
        pass


class TokenBucket(RateLimiter):
    def __init__(self, maxBucketSize, refillRate, refillRateInSeconds):
        self.maxBucketSize = maxBucketSize
        self.currentBucketSize = maxBucketSize
        self.refillRate = refillRate
        self.refillRateInSeconds = refillRateInSeconds
        self.lastRefilledAt = time.time()
    
    def refill(self):
        now = time.time()
        elapsedTime = now - self.lastRefilledAt
        if elapsedTime >= self.refillRateInSeconds:
            self.currentBucketSize = min(self.currentBucketSize + self.refillRate, self.maxBucketSize)
            self.lastRefilledAt = now
    
    def requestHandler(self, requestId, tokens=None):
        print(f'RequestId: {requestId}, currentBucketSize: {self.currentBucketSize}')
        self.refill()
        if not tokens:
            tokens = 1
        
        if self.currentBucketSize >= tokens:
            self.currentBucketSize -= tokens
            print(f'Request {requestId} allowed')
            return True
        
        print(f'Request {requestId} blocked')
        return False


rateLimiter = TokenBucket(5, 5, 1)
for i in range(1, 20):
    rateLimiter.requestHandler(i)
    time.sleep(0.1)
