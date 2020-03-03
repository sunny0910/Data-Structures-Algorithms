from singly_linked_list import LinkedList, Node


class AddNumbers(LinkedList):

    @staticmethod
    def add_two_number(l1, l2):
        """
        Function to add two numbers represented by linked list by a single traversal.
        :param l1: Node
        :param l2: Node
        :return: Node
        """
        num1 = l1
        num2 = l2
        carry = 0
        l3 = None
        l3_tail = None
        
        while num1 or num2:
            total = (num1.data if num1 else 0) + (num2.data if num2 else 0) + carry
            carry = total // 10
            total = total % 10
            node = Node(total)
            if not l3:
                l3 = node
            else:
                l3_tail.next = node
            l3_tail = node
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
        if carry != 0:
            l3.insert(carry)
        return l3


if __name__ == "__main__":
    ll1 = AddNumbers()
    ll1.insert(5)
    ll1.insert(2)
    ll1.insert(5)
    print("Number 1", end=" - ")
    ll1.print_linked_list()
    ll2 = AddNumbers()
    ll2.insert(4)
    ll2.insert(2)
    print("Number 2", end=" - ")
    ll2.print_linked_list()
    ll3 = AddNumbers()
    ll3.head = AddNumbers.add_two_number(ll1.head, ll2.head)
    print("Sum of numbers - ", end=" ")
    ll3.print_linked_list()
