from binary_trees.binary_search_tree import BinarySearchTree


def count_leaf_nodes(root):
    """
    Function to count the number of leaf nodes in a BTree
    :param root: Node
    :return: Int
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


def count_internal_nodes(root):
    """
    Function to count the number of internal nodes in a BTree
    :param root: Node
    :return: Int
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)


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
    internal_nodes = count_internal_nodes(bst.root)
    print(internal_nodes)
    leaf_nodes = count_leaf_nodes(bst.root)
    print(leaf_nodes)