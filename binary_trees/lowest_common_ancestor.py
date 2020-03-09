from binary_trees.binary_search_tree import BinarySearchTree
from binary_trees.path_to_node import path_to_node


def lcs(root, a, b):
    """
    Function to find the lowest common ancestor of two nodes.
    Two nodes will always have a common ancestor in a Bianry Tree.
    :param root: Node
    :param a: Node #target node 1
    :param b: Node #target node 2
    :return: Int #LCS value
    """
    if not root:
        return
    path1 = []
    path2 = []
    path_to_node(root, a, path1)
    path_to_node(root, b, path2)
    i = len(path1) - 1
    j = len(path2) - 1
    while path1[i] == path2[j]:
        i -= 1
        j -= 1
    return path1[i+1]


def optimised_bst_lcs(root, n1, n2):
    """
    Optimised recursive solution for finding the lcs in BST. It traverses the tree only once compared to two traversals
    and one iteration over path array in the above approach.
    :param root: Node
    :param n1: Int
    :param n2: Int
    :return: Node # LCS
    """
    if not root:
        return
    if n1 < root.data and n2 < root.data:
        return optimised_bst_lcs(root.left, n1, n2)
    if n1 > root.data and n2 > root.data:
        return optimised_bst_lcs(root.right, n1, n2)
    return root.data


def optimised_btree_lcs(root, n1, n2):
    """
    Optimised recursive approach for finding the lcs in BTree. It traverses the left and right node of all nodes in the
    tree to check if node matches with n1 and n2.
    If a node matches with any of the nodes then that is returned and the lowest root node which will get both nodes
    present in left and right sub-tree will be returned as LCS.
    This approach assumes that both the nodes are present in the tree.
    :param root: Node
    :param n1: Int
    :param n2: Int
    :return: Node
    """
    if not root:
        return
    if root.data == n1 or root.data == n2:
        return root
    left_lcs = optimised_btree_lcs(root.left, n1, n2)
    right_lcs = optimised_btree_lcs(root.right, n1, n2)
    if left_lcs and right_lcs:
        return root
    return left_lcs or right_lcs


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

    lcs = optimised_bst_lcs(bst.root, 4, 14)
    print(lcs)
    