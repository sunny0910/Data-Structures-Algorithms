from linkedlists.circular_linked_list.circular_linked_list import CircularLinkedList


class MergeSort(CircularLinkedList):

    def merge_sort(self, front, rear):
        if not rear and front:
            return front, front
        if not front and rear:
            return rear, rear
        if front == rear:
            return front, rear
        prev_to_middle, middle = CircularLinkedList.middle_prev_to_middle(front, rear)
        if prev_to_middle:
            prev_to_middle.next = front
        else:
            middle = middle.next
        rear.next = middle
        l1_front, l1_rear = self.merge_sort(front, prev_to_middle)
        l2_front, l2_rear = self.merge_sort(middle, rear)

        l1_rear.next = l2_rear.next = None
        front = self.sorted_merge(l1_front, l2_front)
        if l2_rear.data > l1_rear.data:
            rear = l2_rear
        else:
            rear = l1_rear
        rear.next = front
        return front, rear

    def sorted_merge(self, l1_front, l2_front):
        if not l1_front:
            return l2_front
        if not l2_front:
            return l1_front
        if l1_front.data < l2_front.data:
            temp = l1_front
            temp.next = self.sorted_merge(l1_front.next, l2_front)
        else:
            temp = l2_front
            temp.next = self.sorted_merge(l1_front, l2_front.next)
        return temp


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
    print("sorted list")
    cll.front, cll.rear = cll.merge_sort(cll.front, cll.rear)
    cll.print_linked_list()