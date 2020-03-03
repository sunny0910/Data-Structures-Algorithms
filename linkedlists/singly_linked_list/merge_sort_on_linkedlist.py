from singly_linked_list import LinkedList

class LinkedListMergeSort(LinkedList):

    def merge_sort(self, head):
        """
        Function to perform merge sort on linked list. It divides the linked list in two halves to form sorted halves
        and merges the halves to form a sorted linked list
        :param head: Node
        :return: Node
        """
        if not head:
            return

        def get_middle_prev_to_middle(head):
            """
            Function to find middle and previous to middle node of the linked list
            :param head: Node
            :return: Node
            """
            slow = fast = head
            prev_to_middle = None
            if not head:
                return
            while fast and fast.next:
                prev_to_middle = slow
                slow = slow.next
                fast = fast.next.next
            return slow, prev_to_middle
        middle, prev_to_middle = get_middle_prev_to_middle(head)
        if not prev_to_middle:
            return head
        prev_to_middle.next = None
        head = self.merge_sort(head)
        middle = self.merge_sort(middle)
        return self.merge_sorted_ll_recursive(head, middle)

def merge_sorted_ll_iterative(self, a, b):
    """
    Iterative function to merge two sorted linked list
    :param a: Node
    :param b: Node
    :return: Node
    """
    if not a:
        return b
    if not b:
        return a
    new_head = tail = None
    while a and b:
        if a.data < b.data:
            if not new_head:
                new_head = tail = a
            else:
                tail.next = a
                tail = a
            a = a.next
        else:
            if not new_head:
                new_head = tail = b
            else:
                tail.next = b
                tail = b
            b = b.next
    while a:
        tail.next = a
        tail = a
        a = a.next
    while b:
        tail.next = b
        tail = b
        b = b.next
    tail.next = None
    return new_head

def merge_sorted_ll_recursive(self, a, b):
    """
    Recursive function to merge two sorted linked list.
    Recursive approach looks small and clean as compared to iterative approach
    :param a: Node
    :param b: Node
    :return: Node # new head
    """
    if not a:
        return b
    if not b:
        return a
    if a.data < b.data:
        result = a
        result.next = self.merge_sorted_ll_recursive(a.next, b)
    else:
        result = b
        result.next = self.merge_sorted_ll_recursive(a, b.next)
    return result


if __name__ == "__main__":
    ll1 = LinkedListMergeSort()
    ll1.insert(9)
    ll1.insert(7)
    ll1.insert(5)
    ll1.insert(2)
    ll1.insert(1)
    # ll2 = LinkedListMergeSort()
    ll1.insert(8)
    ll1.insert(6)
    ll1.insert(4)
    ll1.insert(3)
    ll1.insert(0)
    ll1.print_linked_list()
    ll1.head = ll1.merge_sort(ll1.head)
    ll1.print_linked_list()