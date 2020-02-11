class MinHeap:
    """
    A Binary Heap is a Binary Tree with following properties.
    1) It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all
    keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.
    2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all
    keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree.
    Max Binary Heap is similar to MinHeap, where the key at root must be minimum among all keys present in binary heap.
    The same property must be recursively true for all nodes in Binary Heap.
    Below is the implementation of Min Heap.
    Although python provides a library heapq, but it only supports Min Heap by default and Max Heap requires some work
    around.
    """
    def __init__(self):
        self.heap = []

    def parent(self, index):
        """
        As binary heap is represented in an array, parent node of an element can be retrieved using the below formula
        (childIndex - 1) / 2
        :param index: Int #childIndex
        :return: Int #parentIndex
        """
        return (index-1)//2

    def insert(self, key):
        """
        To insert a key in binary heap, we add a new key at the end of the tree. If new key follows the rule (less than
        parent key in Max Heap and greater than parent key in Min Heap) of heap, we don't do anything. Otherwise we
        move the key up the heap to fix the rule violation.
        :param key: Int
        :return: None
        """
        self.heap.append(key)
        if len(self.heap) > 1:
            current = len(self.heap) - 1
            while current > 1 and self.heap[current] < self.heap[self.parent(current)]:
                self.heap[current], self.heap[self.parent(current)] = self.heap[self.parent(current)], self.heap[current]
                current = self.parent(current)

    def remove(self):
        """
        To remove a key in binary heap, we remove the Min/Max key present at index 0, then apply heapification logic
        to balance the heap.
        The formula for the left and right index of a parent node in heap is as below:
        leftChild = 2*parentIndex + 1
        rightChild = 2*parentIndex + 2
        :return: None
        """
        self.heap[0] = self.heap.pop()
        heapLength = len(self.heap)
        minIndex = 0
        leftIndex = 2*minIndex + 1
        rightIndex = 2*minIndex + 2
        while (all(i > heapLength for i in [minIndex, leftIndex, rightIndex]) and (self.heap[minIndex] > self.heap[leftIndex] or self.heap[minIndex] > self.heap[rightIndex])):
            if (self.heap[minIndex] > self.heap[leftIndex]):
                self.heap[minIndex], self.heap[leftIndex] = self.heap[leftIndex], self.heap[minIndex]
                minIndex = 2*minIndex + 1
            else:
                self.heap[minIndex], self.heap[rightIndex] = self.heap[rightIndex], self.heap[minIndex]
                minIndex = 2*minIndex + 2
            leftIndex = 2*minIndex + 1
            rightIndex = 2* minIndex + 2

    def printHeap(self):
        """
        Function to print the heap
        :return: None
        """
        print(self.heap)

heap = MinHeap()
heap.insert(10)
heap.insert(23)
heap.insert(36)
heap.insert(32)
heap.insert(38)
heap.insert(45)
heap.insert(57)
heap.printHeap()
heap.remove()
heap.printHeap()