from collections import deque


class SimpleDB:
    def __init__(self):
        self.mainHashMap = {}
        self.transactionQueue = deque()

    def set(self, key, value):
        """set sets the value associated with the key"""
        if not self.transactionQueue:
            self.mainHashMap[key] = value
            return
        else:
            hashMap = self.transactionQueue[0]
            hashMap[key] = value

    def get(self, key):
        """
        get returns the value associated with the key
        get should raise a KeyError if the key doesn't exist
        """
        for i in range(len(self.transactionQueue), -1, -1):
            if key in self.transactionQueue[i]:
                return self.transactionQueue[i][key]
        
        if key in self.mainHashMap:
            return self.mainHashMap[key]
        
        raise Exception("key not found")

    def unset(self, key):
        """unset should delete the key from the db"""

        if key not in self.mainHashMap:
            raise Exception("key not found")
        
        del self.mainHashMap[key]
        for transactionHashMap in self.transactionQueue:
            if key in transactionHashMap:
                del transactionHashMap[key]

        # setting value as None on unset
        return

    def begin(self):
        """begin starts a new transaction"""
        self.transactionQueue.append({})

    def commit(self):
        """
        commit applies all transactions
        it should raise an Exception if there is no ongoing transaction
        """
        for transactionhashMap in self.transactionQueue:
            for key, value in enumerate(transactionhashMap):
                self.mainHashMap[key] = value
        

    def rollback(self):
        """
        rollback undoes the most recent transaction
        it should raise an Exception if there is no ongoing transaction
        """
        if self.transactionQueue:
            self.transactionQueue.pop()
        else:
            raise Exception("No ongoing transaction")
