class KStacks:
    """
    Implementing K-Stacks in a single array.
    The naive approach is to divide the array in K equal parts and keep track of the top of the stack, but in
    this approach array space wont be fully utilised as stack will get full even though array has space in other stack.

    This approach is to keep top of the stacks in auxiliary arrays of size K each and next elements in another array of
    size N.
    The next array will keep indexes of next element in the stack represented in array.
    Initially every index will point to the next indexed (i -> i+1), but as soon as the stack gets filled the top
    elements will point to the bottom elements.
    """
    def __init__(self, k, n):
        """
        Top array of size K will keep the top of K stacks.
        Next array of size n keep indexes of next element in the stack represented in array.
        Initially every index will point to the next indexed (i -> i+1), but as soon as the stack gets filled the top
        elements will point to the bottom elements.
        :param k: Int
        :param n: Int
        """
        self.n = n
        self.k = k
        self.array = [0] * self.n
        self.top = [-1] * self.k
        self.free = 0
        self.next = [i+1 for i in range(self.n)]
        self.next[-1] = -1

    def is_empty(self, sn):
        """
        If stack number 'sn' is empty
        :param sn: Int
        :return: Bool
        """
        return self.top[sn] == -1

    def is_full(self):
        """
        If array is full
        :return: Bool
        """
        return self.free == -1

    def push(self, item, sn):
        """
        To push a element in the stack number 'sn'.
        It gets the free index (self.free) at which element can be pushed.
        It sets the free index to the next free index using the value of free index in the next array.
        It pushed the element at free index and changes the next value of the current top of the stack in the next
        array to the new top of the stack.
        And lastly it changes the top of the stack.
        :param item: Int
        :param sn: Int
        :return: None
        """
        if self.is_full():
            print("Stack overflow")
            return
        insert_at = self.free

        self.free = self.next[self.free]

        self.array[insert_at] = item

        self.next[insert_at] = self.top[sn]

        self.top[sn] = insert_at

    def pop(self, sn):
        """
        Function to pop the top of the stack 'sn'.
        Retrieves the index of the element to be popped (pop_at)
        Changes the top of the stack to the next element in the stack using the index in the next  array.
        Set the next value of popped element as free in next array and changes the free value.
        Returned the popped value
        :param sn: Int
        :return: Int
        """
        if self.is_empty(sn):
            print("Stack is Empty")
            return

        pop_at = self.top[sn]

        self.top[sn] = self.next[pop_at]

        self.next[pop_at] = self.free

        self.free = pop_at

        return self.array[pop_at]

    def print_stack(self, sn):
        """
        Function to print the stack in top-down order
        :param sn: Int
        :return: None
        """
        top_index = self.top[sn]
        while top_index != -1:
            print(self.array[top_index])
            top_index = self.next[top_index]


kstacks = KStacks(3, 10)

kstacks.push(15, 2)
kstacks.push(45, 2)

kstacks.push(17, 1)
kstacks.push(49, 1)
kstacks.push(39, 1)

kstacks.push(11, 0)
kstacks.push(9, 0)
kstacks.push(7, 0)

print("Popped element from stack 2 is ".format(kstacks.pop(2)))
kstacks.print_stack(2)
print("Popped element from stack 1 is ".format(kstacks.pop(1)))
kstacks.print_stack(1)
print("Popped element from stack 0 is ".format(kstacks.pop(0)))
kstacks.print_stack(0)
