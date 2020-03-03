from singly_linked_list import LinkedList


class LinkedListReverse(LinkedList):

    @staticmethod
    def iterative_reverse(head):
        """
        Iterative function to reverse the linked list.
        It uses previous, current, and next pointers
        :param head: Node # old head
        :return: Node # New head
        """
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    @staticmethod
    def recursive_reverse(head, prev=None):
        """
        Recursive function to reverse a linked list.
        :param head:
        :param prev:
        :return:
        """
        if not head:
            return prev
        else:
            next = head.next
            head.next = prev
            return LinkedListReverse.recursive_reverse(next, head)


if __name__ == "__main__":
    ll = LinkedListReverse()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.print_linked_list()
    ll.head = ll.iterative_reverse(ll.head)
    ll.print_linked_list()
    ll.head = ll.recursive_reverse(ll.head)
    ll.print_linked_list()
