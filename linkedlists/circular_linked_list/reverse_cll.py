from linkedlists.circular_linked_list.circular_linked_list import CircularLinkedList


class Reverse(CircularLinkedList):

    def reverse(self):
        curr = self.rear.next
        prev = self.rear
        while True:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if curr == self.front:
                self.front = prev
                self.rear = curr
                print("linked list reversed")
                return


if __name__ == "__main__":
    cll = Reverse()
    cll.insert_at_start(4)
    cll.insert_at_start(3)
    cll.insert_at_start(2)
    cll.insert_at_start(1)
    cll.insert_at_end(5)
    cll.insert_at_end(6)
    cll.insert_after_value(7, 6)
    cll.insert_after_value(0, 1)
    cll.print_linked_list()
    cll.reverse()
    cll.print_linked_list()
