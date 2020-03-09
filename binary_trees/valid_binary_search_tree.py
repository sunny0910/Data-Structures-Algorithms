from binary_trees.binary_search_tree import BinarySearchTree


def valid_bst(root, left=None, right=None):
    """
    Recursive function to check whether tree is a valid binary search tree or not.
    :param root: Node
    :param left: Node
    :param right: Node
    :return: Bool
    """
    if not root:
        return True
    if left and left.data > root.data or right and right.data < root.data:
        return False
    return valid_bst(root.left, left, root) and valid_bst(root.right, root, right)


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
    x = valid_bst(bst.root)
    print(x)
