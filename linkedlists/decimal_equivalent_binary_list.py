class Node:
    """
    Linked list node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def decimal_equivalent(self):
        """
        Function to get the decimal equivalent of a binary number represented by a linked list
        It fetches the number from linked list to a array and applies the decimal to binary conversion on the list.
        :return: Int
        """
        if not self.head:
            return 0
        numbers = []
        temp = self.head
        while temp:
            numbers.append(temp.data)
            temp = temp.next
        n = len(numbers) - 1
        decimal = 0
        for index, number in enumerate(numbers):
            if number == 1:
                decimal += 2**(n-index)
        return decimal


ll = LinkedList()
ll.add(0)
ll.add(0)
ll.add(1)
# ll.add(0)
# ll.add(1)
# ll.add(1)
# ll.add(0)
# ll.add(0)
# ll.add(0)
ll.print()
x = ll.decimal_equivalent()
print(x)
