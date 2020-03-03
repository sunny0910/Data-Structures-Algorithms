class Node:
    """
    LinkedLIst node with data and next pointer attributes
    """
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Inserts a new node in a linked list.
        Insertion happens from beginning always
        :param data: Int
        :return: None
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_linked_list(self):
        """
        Function to print all the elements of linked list.
        :return: None
        """
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def delete(self, data):
        """
        Function to delete a element from the linked list.
        :param data: Int
        :return: None
        """
        prev = None
        curr = self.head
        while curr:
            if curr.data == data:
                break
            else:
                prev = curr
                curr = curr.next
        if not curr:
            print('Element not found')
            return
        if not prev:
            self.head = self.head.next
        elif not curr.next:
            prev.next = None
        else:
            prev.next = curr.next
        curr.next = None

    def get_middle(self):
        """
        Function to get the middle of the linked list.
        It uses floyd's cyclic algorithm with slow and fast pointer which moves with one and two elements respectively,
        and slow pointer ends up on the middle of the linked list
        :return: None
        """
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)


    def detect_loop(self):
        """
        Function to detect loop in a linked list
        :return: Bool
        """
        # nodes_dict = {}
        # temp = self.head
        # while temp:
        #     if temp.data in nodes_dict:
        #         return True
        #     nodes_dict[temp.data] = True
        #     temp = temp.next
        # return False
        slow = self.head
        fast = self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                print(slow.data)
                return True
        return False

    def correct_loop(self):
        """
        Function to correct the loop in a linked list.
        It first finds the loop node using floyd's cyclic algorithm and using the slow pointer node and first pointer,
        finds the node where the loops ends and corrects the loop
        :return: None
        """
        def node_reachable(start, loop_node):
            while start:
                if start.data == loop_node.data:
                    return True
                start = start.next
            return False

        loop_node = None
        slow = fast = self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                loop_node = slow
                break
        start = self.head
        while not node_reachable(start.next, loop_node):
            loop_node = loop_node.next
        loop_node.next = None


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert(2)
    ll1.insert(3)
    ll1.insert(1)
    ll1.insert(5)
    ll1.insert(7)
    ll1.insert(6)
    # ll2.insert(8)
    # ll2.head = Node(4)
    # ll2.head.next = Node(8)
    # ll2.head.next.next = Node(1)
    # ll2.head.next.next.next = Node(2)
    # ll2.head.next.next.next.next = ll2.head.next

    # ll.insert(1)
    # ll.insert(0)
    # ll.insert(0)
    ll1.print_linked_list()
    ll1.delete(2)
    # ll.separate_even_odd_numbers()
    # ll.iteratetive_reverse()
    # ll.check_palindrome_using_reverse()
    # ll.head = ll.k_nodes_reverse(ll.head, 3)
    # ll1.head = ll1.merge_sort(ll1.head)
    ll1.print_linked_list()
    # l3 = LinkedList()
    # l3.head = LinkedList.add_two_number(ll1.head, ll2.head)
    # l3.print_linked_list()
