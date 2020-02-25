class TwoStacks:
    """
    Function to implement two stacks in a array.
    Two stacks will start from index 0 and index n-1 and keep pushing the new elements in the middle of the array
    until their is not space left between the top of stack1 and stack2.
    Index of top of two stacks will be saved using two variables top1 and top2.
    """

    def __init__(self, n):
        """
        array of size n to store elements of the stack.
        top1 and top2 to store indexes of the top of the stack.
        """
        self.array = [None] * n
        self.top1 = -1
        self.top2 = len(self.array)

    def push1(self, x):
        """
        Function to push element in the stack.
        It checks the difference between indexes of the two tops to check for stack full.
        If not, it increments the stack top index and pushed the element in the array.
        :param x: Int
        :return: None
        """
        if self.top2-1 == self.top1:
            print("Memory out of bound")
        else:
            self.top1 += 1
            self.array[self.top1] = x

    def push2(self, x):
        """
        Function to push element in the stack.
        It checks the difference between indexes of the two tops to check for stack full.
        If not, it increments the stack top index and pushed the element in the array.
        :param x: int
        :return: None
        """
        if self.top2-1 == self.top1:
            print("Memory out of bound")
        else:
            self.top2 -= 1
            self.array[self.top2] = x

    def pop1(self):
        """
        Function to pop the element from the stack.
        It check the stack index to check for empty stack.
        It not, it removes the element at the stack top and decrement the index of stack top
        :return: Int
        """
        if self.top1 >= 0:
            x = self.array[self.top1]
            self.array[self.top1] = None
            self.top1 -= 1
            return x
        else:
            print("Stack underflow")

    def pop2(self):
        """
        Function to pop the element from the stack.
        It check the stack index to check for empty stack.
        It not, it removes the element at the stack top and decrement the index of stack top
        :return: Int
        """
        if self.top2 <= len(self.array) - 1:
            x = self.array[self.top2]
            self.array[self.top2] = None
            self.top2 += 1
            return x
        else:
            print("Stack underflow")


two_stacks = TwoStacks(6)
two_stacks.push1(1)
two_stacks.push1(2)
two_stacks.push1(3)
two_stacks.push1(4)
print(two_stacks.array)
two_stacks.push2(9)
two_stacks.push2(8)
two_stacks.pop1()
two_stacks.push2(7)
print(two_stacks.array)
