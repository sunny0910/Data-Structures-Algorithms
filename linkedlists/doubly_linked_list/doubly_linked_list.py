class Node:
    """
    Node of a doubly linked list with data, previous, and next pointer attributes
    """
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        """
        Function to insert a node at the start of a DLL
        :param data: Int
        :return: None
        """
        if not data:
            return
        node = Node(data)
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def insert_at_end(self, data):
        """
        Function to insert a node at the end of a DLL
        :param data: Int
        :return: None
        """
        if not data:
            return
        node = Node(data)
        if not self.head:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        node.prev = last

    def insert_middle(self, data, target, before=False):
        """
        Function to insert a node in the middle of a linked list.
        :param data: Int
        :param target: Int
        :param before: Bool # before or after the target node
        :return: None
        """
        if not target or not data:
            return
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        if before:
            # Insert before target
            while temp and temp.next and temp.next.data != target:
                temp = temp.next
        else:
            # Insert after target
            while temp and temp.data != target:
                temp = temp.next
        if not temp:
            # target not found
            return
        node.next = temp.next
        if temp.next:
            temp.next.prev = node
        temp.next = node
        node.prev = temp
        return

    def delete(self, node):
        """
        Function to delete a node in the linked list
        :param node: Node
        :return: None
        """
        target = self.head
        prev_to_target = None
        while target and target.data != node:
            prev_to_target = target
            target = target.next
        if not target:
            return
        if not prev_to_target:
            target.next.prev = None
            self.head = target.next
            return
        elif not target.next:
            prev_to_target.next = None
            return
        else:
            prev_to_target.next = target.next
            target.next.prev = prev_to_target
        target.next = None
        target.prev = None
        return

    def print_list(self):
        """
        Function to print the elements in the linked list
        :return: None
        """
        temp = self.head
        last = None
        print("From Forward", end=" - ")
        while temp:
            print(temp.data, end=" ")
            last = temp
            temp = temp.next
        print()
        print("From Backward", end=" - ")
        while last:
            print(last.data, end=" ")
            last = last.prev
        print()

    @staticmethod
    def get_middle(head):
        """
        Function to get the middle of the linked list
        :param head: Node
        :return: Node
        """
        if not head:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    dll1 = DoublyLinkedList()
    dll1.insert_at_start(1)
    dll1.insert_middle(3, 1, False)
    dll1.insert_at_end(5)
    dll1.insert_at_end(7)
    dll1.insert_at_end(9)
    dll1.delete(9)
    dll1.print_list()
    x = dll1.get_middle(dll1.head)
    print(x.data)
