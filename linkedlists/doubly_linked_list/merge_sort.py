from doubly_linked_list import DoublyLinkedList


class MergeSort(DoublyLinkedList):
    
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
            result.next = MergeSort.merge_sorted_lists(first.next, second)
        else:
            result = second
            result.next = MergeSort.merge_sorted_lists(first, second.next)
        result.next.prev = result
        return result

    def merge_sort(self, head):
        """
        Recursive function to perform merge sort on a DLL
        :param head: Node
        :return: Node # new head
        """
        if not head or not head.next:
            return head
        middle = DoublyLinkedList.get_middle(head)
        middle.prev.next = None
        middle.prev = None
        head = self.merge_sort(head)
        middle = self.merge_sort(middle)
        return MergeSort.merge_sorted_lists(head, middle)


if __name__ == "__main__":
    dll1 = MergeSort()
    dll1.insert_at_end(7)
    dll1.insert_at_start(1)
    dll1.insert_at_end(10)
    dll1.insert_at_end(4)
    dll1.insert_at_end(9)
    dll1.insert_middle(3, 1, False)
    dll1.insert_at_end(8)
    dll1.insert_at_end(2)
    dll1.insert_at_end(5)
    dll1.print_list()
    dll1.head = dll1.merge_sort(dll1.head)
    dll1.print_list()
