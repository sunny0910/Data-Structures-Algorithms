class Kstack:
    def __init__(self, k, n) -> None:
        self.n = n
        self.k = k
        
        self.arr = [0] * self.n
        
        self.top = [-1] * self.k
        
        self.free = 0
        
        self.next = [i+1 for i in range(self.n)]
        self.next[self.n-1] = -1
        
    def isEmpty(self, sn):
        return self.top[sn] == -1
    
    def isFull(self):
        return self.free == -1
    
    def push(self, sn, item):
        if self.isFull():
            return "stack full"
        
        # index to be inserted at
        insert_at = self.free
        
        # changing the free index taken from next of free
        self.free = self.next[self.free]
        
        # setting the array item
        self.arr[insert_at] = item
        
        # getting the current top of the stack
        current_top = self.top[sn]
        
        # setting the next of insert_at index to current top in top to bottom order
        self.next[insert_at] = current_top
        
        # changing the top of the stack
        self.top[sn] = insert_at
        
    def pop(self, sn):
        if self.isEmpty(sn):
            return "stack is empty"
        
        # get top of stack from top array
        currentTop = self.top[sn]
        # the next index of top would be new top so update top
        newTopIndex = self.next[currentTop]
        # set the index of item as free and set next of free as index
        self.next[currentTop] = self.free
        self.free = currentTop
        # set arr element as -1
        self.arr[currentTop] = -1
        # update top index
        self.top[sn] = newTopIndex
