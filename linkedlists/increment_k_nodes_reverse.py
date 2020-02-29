class Node:
    """
    Linked list Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def k_reverse(self, head, k):
        """
        Function to print k reverse of the linked list in incremental order.
        Initially K will be 1 and then incremented in every recursive call until the end of the linked list in reached.
        The approach is similar to K node reverse approach with only difference here is that we increment K value in
        every recursive call.
        :param head: Node
        :param k: Int
        :return: Node
        """
        if not head:
            return
        if k % 2 == 0:
            temp = head
            count = 0
            while temp and count < k-1:
                temp = temp.next
                count += 1
            if temp:
                temp.next = self.k_reverse(temp.next, k + 1)
            return head
        prev = None
        curr = head
        count = 0
        while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        if curr:
            head.next = self.k_reverse(curr, k + 1)
        return prev


ll = LinkedList()
ll.add(7)
ll.add(6)
ll.add(5)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)
ll.print_linked_list()
ll.head = ll.k_reverse(ll.head, 1)
ll.print_linked_list()
