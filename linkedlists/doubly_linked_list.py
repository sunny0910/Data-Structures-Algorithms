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
        print("In forward")
        while temp:
            print(temp.data, end=" ")
            last = temp
            temp = temp.next
        print()
        print("In Backward")
        while last:
            print(last.data, end=" ")
            last = last.prev
        print()

    def reverse(self):
        """
        Function to reverse a linked list
        :return: None
        """
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        self.head = prev
        return

    @staticmethod
    def merge_sorted_lists(first, second):
        """
        Function to merge sorted linked list in-place
        :param first: Node
        :param second: Node
        :return: Node # new head
        """
        if not first:
            return second
        if not second:
            return first
        if first.data < second.data:
            result = first
            result.next = DoublyLinkedList.merge_sorted_lists(first.next, second)
        else:
            result = second
            result.next = DoublyLinkedList.merge_sorted_lists(first, second.next)
        result.next.prev = result
        return result

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

    def merge_sort(self, head):
        """
        Recursive function to perform merge sort on a DLL
        :param head: Node
        :return: Node # new head
        """
        if not head or not head.next:
            return head
        middle = self.get_middle(head)
        middle.prev.next = None
        middle.prev = None
        head = self.merge_sort(head)
        middle = self.merge_sort(middle)
        return DoublyLinkedList.merge_sorted_lists(head, middle)


dll1 = DoublyLinkedList()
dll1.insert_at_start(1)
dll1.insert_middle(3, 1, False)
dll1.insert_at_end(5)
dll1.insert_at_end(7)
dll1.insert_at_end(9)
dll1.delete(9)
dll1.print_list()
dll2 = DoublyLinkedList()
dll2.insert_at_end(2)
dll2.insert_at_end(4)
dll2.insert_middle(6, 8, True)
dll2.insert_at_end(8)
dll2.insert_at_end(10)
dll2.delete(4)
# dll2.reverse()
dll2.print_list()
dll3 = DoublyLinkedList()
dll3.head = DoublyLinkedList.merge_sorted_lists(dll1.head, dll2.head)
dll3.print_list()
dll4 = DoublyLinkedList()
dll4.insert_at_end(7)
dll4.insert_at_end(1)
dll4.insert_at_end(5)
dll4.insert_at_end(2)
dll4.insert_at_end(10)
dll4.insert_at_end(8)
dll4.print_list()
dll4.head = dll4.merge_sort(dll4.head)
dll4.print_list()
