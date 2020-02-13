class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def delete(self, data):
        prev = None
        curr = self.head
        while curr:
            if curr.data == data:
                break
            else:
                prev = curr
                curr = curr.next
        if not curr:
            print('Element not found')
            return
        if not prev:
            self.head = self.head.next
        elif not curr.next:
            prev.next = None
        else:
            prev.next = curr.next
        curr.next = None

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    def iterative_reverse(self, head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def recursive_reverse(self, head, prev):
        if not head:
            return prev
        else:
            next = head.next
            head.next = prev
            return self.recursive_reverse(next, head)

    def k_nodes_reverse(self, head, k):
        curr = head
        prev = None
        count = 0
        while curr and count < k:
            count += 1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if curr:
            head.next = self.k_nodes_reverse(curr, k)
        return prev

    def check_palindrome_using_stack(self):
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
        second_half = self.iterative_reverse(second_half)
        res = LinkedList.compare_list(self.head, second_half)
        second_half = self.iterative_reverse(second_half)
        if midnode:
            prev_to_slow.next = midnode
            midnode.next = second_half
        else:
            prev_to_slow.next = second_half
        return res

    def dutch_national_flag_problem(self):
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

    def separate_end_odd_numbers(self):
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

    @staticmethod
    def add_two_number(l1, l2):
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

    def detect_loop(self):
        # nodes_dict = {}
        # temp = self.head
        # while temp:
        #     if temp.data in nodes_dict:
        #         return True
        #     nodes_dict[temp.data] = True
        #     temp = temp.next
        # return False
        slow = self.head
        fast = self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                print(slow.data)
                return True
        return False

    def correct_loop(self):
        def node_reachable(start, loop_node):
            while start:
                if start.data == loop_node.data:
                    return True
                start = start.next
            return False

        loop_node = None
        slow = fast = self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                loop_node = slow
                break
        start = self.head
        while not node_reachable(start.next, loop_node):
            loop_node = loop_node.next
        loop_node.next = None

    def merge_sort(self, head):
        if not head:
            return

        def get_middle_prev_to_middle(head):
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


ll1 = LinkedList()
ll2 = LinkedList()
ll1.insert(2)
ll1.insert(3)
ll1.insert(1)
ll1.insert(5)
ll1.insert(7)
ll1.insert(6)
# ll2.insert(8)
# ll2.head = Node(4)
# ll2.head.next = Node(8)
# ll2.head.next.next = Node(1)
# ll2.head.next.next.next = Node(2)
# ll2.head.next.next.next.next = ll2.head.next

# ll.insert(1)
# ll.insert(0)
# ll.insert(0)
ll1.print_linkedlist()
# ll.delete(2)
# ll.separate_end_odd_numbers()
# ll.iteratetive_reverse()
# ll.check_palindrome_using_reverse()
# ll.head = ll.k_nodes_reverse(ll.head, 3)
ll1.head = ll1.merge_sort(ll1.head)
ll1.print_linkedlist()
# l3 = LinkedList()
# l3.head = LinkedList.add_two_number(ll1.head, ll2.head)
# l3.print_linkedlist()
