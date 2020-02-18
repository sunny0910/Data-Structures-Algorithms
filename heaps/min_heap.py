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
        heap_length = len(self.heap)
        min_index = 0
        left_index = (2 * min_index) + 1
        right_index = (2 * min_index) + 2
        while all(i > heap_length for i in [min_index, left_index, right_index]) \
                and (self.heap[min_index] > self.heap[left_index] or self.heap[min_index] > self.heap[right_index]):
            if self.heap[min_index] > self.heap[left_index]:
                self.heap[min_index], self.heap[left_index] = self.heap[left_index], self.heap[min_index]
                min_index = (2 * min_index) + 1
            else:
                self.heap[min_index], self.heap[right_index] = self.heap[right_index], self.heap[min_index]
                min_index = (2 * min_index) + 2
            left_index = (2 * min_index) + 1
            right_index = (2 * min_index) + 2

    def print_heap(self):
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
heap.print_heap()
heap.remove()
heap.print_heap()
