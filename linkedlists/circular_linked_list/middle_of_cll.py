from linkedlists.circular_linked_list.circular_linked_list import CircularLinkedList


class Middle(CircularLinkedList):

    def get_middle(self):
        """
        To get the middle element of the circular linked list. It uses floyd's circular algorithm with slow and fast
        pointer.
        :return: Node
        """
        slow = fast = self.rear.next
        while fast and fast.next:
            if fast.next == self.front or fast.next.next == self.front:
                break
            slow = slow.next
            fast = fast.next.next
        print("middle of list is {}".format(slow.data))
        return slow


if __name__ == "__main__":
    cll = Middle()
    cll.insert_at_start(4)
    cll.insert_at_start(3)
    cll.insert_at_start(2)
    cll.insert_at_start(1)
    cll.insert_at_end(5)
    cll.insert_at_end(6)
    cll.insert_after_value(7, 6)
    cll.insert_after_value(0, 1)
    cll.insert_after_value(9, 10)
    cll.print_linked_list()
    cll.get_middle()
