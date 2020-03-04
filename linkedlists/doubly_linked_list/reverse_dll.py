from doubly_linked_list import DoublyLinkedList


class DllReverse(DoublyLinkedList):
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


if __name__ == "__main__":
    dll = DllReverse()
    dll.insert_at_start(1)
    dll.insert_middle(3, 1, False)
    dll.insert_at_end(5)
    dll.insert_at_end(7)
    dll.insert_at_end(9)
    dll.print_list()
    dll.reverse()
    dll.print_list()
