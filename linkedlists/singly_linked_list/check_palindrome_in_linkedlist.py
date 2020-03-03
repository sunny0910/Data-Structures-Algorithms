from singly_linked_list import LinkedList
from reverse_linkedlist import LinkedListReverse


class CheckPalindrome(LinkedList):
    
    def check_palindrome_using_stack(self):
        """
        Function to check whether elements in linked list form a palindrome of not.
        It traverses the linked list twice, once to push all elements in stack and other to verify elements in the stack
        :return: Bool
        """
        stack = []
        temp = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.next
        temp = self.head
        while temp:
            if temp.data != stack[0]:
                return False
            stack.pop(0)
            temp = temp.next
        return True

    @staticmethod
    def compare_list(first, second):
        """
        Function to compare elements of the two list
        :param first: Node
        :param second: Node
        :return: Bool
        """
        temp1 = first
        temp2 = second
        while temp1 and temp2:
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return False
        if not temp1 and not temp2:
            return True
        return False

    def check_palindrome_using_reverse(self):
        """
        Function to check whether elements in the liked list form a palindrome or not.
        This function gets to the middle of linked list and reverses the second half to check it it matches with the
        first half. It reverses the second half again to form the second half
        :return: Bool
        """
        slow = self.head
        fast = self.head
        midnode = None
        prev_to_slow = None
        while fast and fast.next:
            prev_to_slow = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            midnode = slow
            slow = slow.next
        prev_to_slow.next = None
        second_half = slow
        second_half = LinkedListReverse.iterative_reverse(second_half)
        res = CheckPalindrome.compare_list(self.head, second_half)
        second_half = LinkedListReverse.iterative_reverse(second_half)
        if midnode:
            prev_to_slow.next = midnode
            midnode.next = second_half
        else:
            prev_to_slow.next = second_half
        return res


if __name__ == "__main__":
    ll = CheckPalindrome()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_linked_list()
    x = ll.check_palindrome_using_stack()
    print(x)
    ll.insert(6)
    ll.print_linked_list()
    x = ll.check_palindrome_using_reverse()
    print(x)
