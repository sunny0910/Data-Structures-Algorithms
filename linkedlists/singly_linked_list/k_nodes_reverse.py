from singly_linked_list import LinkedList

class KNodesReverse(LinkedList):

    def k_nodes_reverse(self, head, k):
        """
        Iterative function to perform K node reverse on a linked list.
        :param head: Node
        :param k: Int
        :return: Node
        """
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


ll = KNodesReverse()
ll.insert(6)
ll.insert(5)
ll.insert(4)
ll.insert(3)
ll.insert(2)
ll.insert(1)
ll.print_linked_list()
ll.head = ll.k_nodes_reverse(ll.head, 2)
ll.print_linked_list()
