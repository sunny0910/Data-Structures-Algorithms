from linkedlists.singly_linked_list.singly_linked_list import Node


class CircularLinkedList:
    """
    Circular linked list which has its last node's next pointed to the first node making it a complete circle.
    """
    def __init__(self):
        """
        Front and rear pointers to keep track of front and rear ends of circular linked list
        """
        self.front = None
        self.rear = None

    def insert_at_end(self, item):
        """
        To insert a node at the end of the circular linked list
        :param item: Int
        :return: None
        """
        node = Node(item)
        if not self.front:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        node.next = self.front

    def insert_at_start(self, item):
        """
        To insert a node at the start of the circular linked list
        :param item: Int
        :return: None
        """
        node = Node(item)
        node.next = self.front
        self.front = node
        if not self.rear:
            self.rear = node
            self.rear = self.front

    def insert_after_value(self, item, value):
        """
        To insert a node in the middle of the circular linked list after the specified value
        :param item: Int
        :param value: Int
        :return: None
        """
        node = Node(item)
        temp = self.rear.next
        while temp.data != value:
            temp = temp.next
            if temp == self.front:
                print("Value {} not found".format(value))
                return
        if temp == self.rear:
            self.rear = node
        node.next = temp.next
        temp.next = node

    def delete_node(self, item):
        """
        To delete a node in the circular linked list. The node could be start, end or a middle node.
        :param item: Int
        :return: None
        """
        if not self.front or not self.rear:
            print("node not found")
            return
        temp = self.rear.next
        previous_to_temp = self.rear
        while temp.data != item:
            previous_to_temp = temp
            temp = temp.next
            if temp == self.front:
                print("{} not found".format(item))
                return
                break
        if temp == self.rear:
            self.rear = previous_to_temp
        if temp == self.front:
            self.front = temp.next
        previous_to_temp.next = temp.next
        temp.next = None
        print("Node {} deleted".format(item))

    def print_linked_list(self):
        """
        To print the nodes in circular linked list
        :return:
        """
        temp = self.rear.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:
                break
        print()

    @staticmethod
    def middle_prev_to_middle(front, rear):
        slow = fast = rear.next
        prev_to_slow = None
        while True:
            if fast.next == front or fast.next.next == front:
                break
            prev_to_slow = slow
            slow = slow.next
            fast = fast.next.next
        return prev_to_slow, slow


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_start(4)
    cll.insert_at_start(1)
    cll.insert_at_start(2)
    cll.insert_at_start(3)
    cll.insert_at_end(6)
    cll.insert_at_end(5)
    cll.insert_after_value(7, 6)
    cll.insert_after_value(0, 1)
    cll.print_linked_list()
    cll.delete_node(1)
    cll.delete_node(7)
    cll.delete_node(5)
    cll.print_linked_list()
