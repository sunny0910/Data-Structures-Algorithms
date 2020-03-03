from singly_linked_list import LinkedList


class DNFLinkedList(LinkedList):

    
    def dutch_national_flag_problem(self):
        """
        Dutch national flag problem to separate 0's, 1's, and 2's in a linked list.
        :return: None
        """
        zero_start = zero_end = None
        one_start = one_end = None
        two_start = two_end = None
        temp = self.head
        while temp:
            if temp.data == 0:
                if not zero_start:
                    zero_start = temp
                    zero_end = temp
                else:
                    zero_end.next = temp
                    zero_end = temp
            if temp.data == 1:
                if not one_start:
                    one_start = temp
                    one_end = temp
                else:
                    one_end.next = temp
                    one_end = temp
            if temp.data == 2:
                if not two_start:
                    two_start = temp
                    two_end = temp
                else:
                    two_end.next = temp
                    two_end = temp
            temp = temp.next
        zero_end.next = one_start
        one_end.next = two_start
        two_end.next = None
        self.head = zero_start

    def separate_even_odd_numbers(self):
        """
        Function to separate event and odd numbers in a linked list
        :return: None
        """
        even_start = even_end = None
        odd_start = odd_end = None
        temp = self.head
        while temp:
            if temp.data % 2 == 0:
                if not even_start:
                    even_start = temp
                else:
                    even_end.next = temp
                even_end = temp
            if temp.data % 2 == 1:
                if not odd_start:
                    odd_start = temp
                else:
                    odd_end.next = temp
                odd_end = temp
            temp = temp.next
        even_end.next = odd_start
        odd_end.next = None
        self.head = even_start


if __name__ == "__main__":
    ll = DNFLinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(1)
    ll.insert(2)
    ll.insert(0)
    ll.print_linked_list()
    ll.dutch_national_flag_problem()
    ll.print_linked_list()
    ll.separate_even_odd_numbers()
    ll.print_linked_list()