from linkedlists.singly_linked_list.singly_linked_list import LinkedList
from binary_trees.binary_search_tree import BinarySearchTree


def binary_tree_to_dll(root, ll):
    """
    Approach #1 to convert a binary tree to doubly linked list.
    In this approach, a head pointer of linked list is maintained to insert nodes in the linked list.
    While doing in-order traversal of the tree with right sub-tree first and then left sub-tree, every node is
    visited and inserted into the linked list.
    This way rightmost element will be inserted first and leftmost element last and nodes will be inserted in the linked
    list in reverse in-order fashion.
    The head will be present at last inserted node hence linked list will be in-order.
    :param root: Node
    :param ll: LinkedList
    :return: None
    """
    if not root:
        return
    binary_tree_to_dll(root.right, ll)
    if ll.head:
        ll.head.left = root
        root.right = ll.head
    ll.head = root
    binary_tree_to_dll(root.left, ll)


def btree_to_dll(root):
    """
    Approach #2 to convert a binary tree to doubly linked list.
    In this approach, a recursive function is used to convert the binary tree to doubly linked list and
    the leftmost node is searched and returned as the head pointer of LinkedList.
    :param root: Node
    :return: Node #linkedlist head
    """

    def btree_to_dll_util(root):
        """
        Recursive function to traverse every node and find the left and right node of it and make the left and right
        pointers to make it a doubly linked list.
        :param root: Node
        :return: Node
        """
        if not root:
            return
        if root.left:
            left = btree_to_dll_util(root.left)
            while left.right:
                left = left.right
            left.right = root
            root.left = left
        if root.right:
            right = btree_to_dll(root.right)
            while right.left:
                right = right.left
            right.left = root
            root.right = right
        return root
    if not root:
        return
    root = btree_to_dll_util(root)
    while root.left:
        root = root.left
    return root


def print_linkedlist(head):
    """
    Function to print every ndoe in linked list
    :param head: Linkedlist.head
    :return: None
    """
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.right
    print()


if __name__ == "__main__":
    
    bst = BinarySearchTree()
    tree_nodes = [20, 8, 4, 12, 10, 14, 22, 25]
    """
    Tree representation of above numbers
                20
               /  \
              8    22
             / \     \
            4  12     25
               / \
              10  14

    in-order traversal - 4, 8, 10, 12, 14, 20, 22, 25
    """
    for node_data in tree_nodes:
        bst.root = bst.insert(bst.root, node_data)

    ll = LinkedList()
    binary_tree_to_dll(bst.root, ll)
    print_linkedlist(ll.head)
