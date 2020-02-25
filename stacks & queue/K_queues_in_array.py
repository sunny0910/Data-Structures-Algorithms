class KQueues:
    """
    Implementing K-Queues in a single array.
    The naive approach is to divide the array in K equal parts and keep track of the start and end of the queue, but in
    this approach array space wont be fully utilised as queue will get full even though array has space in other queues.

    This approach is to keep front and rear of the queues in two arrays of size K and next elements in another array of
    size N. The auxiliary space seems higher in this approach, but space will be fully utilized in this approach as
    queue will only get full when all elements in the array are occupied.
    """

    def __init__(self, n, k):
        """
        Front and rear array of size K keeps the front and rear of K queues.
        Next array of size n keeps index of next element for every element in the array.
        Free variable keeps the index of next free variable in the array.
        :param n: Int
        :param k: Int
        """
        self.k = k
        self.n = n
        self.array = [0] * self.n
        self.front = [-1] * self.k
        self.rear = [-1] * self.k
        self.next = [i+1 for i in range(self.n)]
        self.next[-1] = -1
        self.free = 0

    def is_empty(self, sn):
        """
        If queue number sn is empty
        :param sn: Int
        :return: Bool
        """
        return self.front[sn-1] == -1

    def is_full(self):
        """
        If array is full
        :return: Bool
        """
        return self.free == -1

    def append(self, sn, item):
        """
        To append the item in the queue number 'sn'.
        It gets the free index from free variable, gets the queue end from rear array, changes the next index of the
        queue end to the free index and changes the array and end arrays with the new values.
        :param sn: Int
        :param item: Int
        :return: None
        """
        if self.is_full():
            print("Queue full")
            return
        insert_at = self.free
        self.free = self.next[insert_at]
        if self.front[sn-1] == -1:
            self.front[sn-1] = insert_at
        if self.rear[sn - 1] != -1:
            queue_end = self.rear[sn - 1]
            self.next[queue_end] = insert_at
        self.rear[sn - 1] = insert_at
        self.next[insert_at] = -1
        self.array[insert_at] = item
    
    def remove(self, sn):
        """
        To remove one element at front from the queue 'sn'.
        It gets the index of the element to be removed from the front array, the index of next element from the
        next array, changes the next of element to be removed as free and assigns the index to self.free.
        Changes the front of the queue and removes the element from the array.
        :param sn: Int
        :return: Int # removed element
        """
        if self.is_empty(sn):
            print("Queue empty")
            return
        remove_at = self.front[sn-1]
        next_element = self.next[remove_at]
        self.next[remove_at] = self.free
        self.free = remove_at
        self.front[sn-1] = next_element
        element = self.array[remove_at]
        self.array[remove_at] = 0
        return element

    def print_queue(self, sn):
        """
        Function to print the queue number 'sn'
        It fetches the front from the self.front and keeps on printing until the end is reached.
        :param sn: Int
        :return: None
        """
        if self.is_empty(sn):
            print("Empty queue")
            return
        queue_start = self.front[sn-1]
        while queue_start != -1:
            print(self.array[queue_start], end=" ")
            queue_start = self.next[queue_start]
        print()


queues = KQueues(9, 3)
queues.append(1, 11)
queues.append(1, 12)
queues.append(1, 13)
queues.print_queue(1)
queues.append(2, 21)
queues.append(2, 22)
queues.append(2, 23)
queues.print_queue(2)
queues.append(3, 31)
queues.print_queue(3)

queues.remove(3)
queues.print_queue(3)
queues.remove(2)
queues.print_queue(2)
queues.remove(1)
queues.remove(1)
queues.print_queue(1)
