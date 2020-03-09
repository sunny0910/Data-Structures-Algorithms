from binary_trees.binary_search_tree import BinarySearchTree


def is_sum_tree(root):
    """
    Function to check whether the tree is a sum tree or not
    :param root: Node
    :return: Bool
    """

    def get_sum(root):
        """
        Utility function to get the sum of the tree starting from the given root recursively.
        :param root: Node
        :return: Int
        """
        if not root:
            return 0
        return root.data + get_sum(root.left) + get_sum(root.right)

    if not root:
        return True
    l_sum = get_sum(root.left)
    r_sum = get_sum(root.right)
    if (root.left or root.right) and root.data != (l_sum+r_sum):
        return False
    return True


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
    x = is_sum_tree(bst.root)
    print(x)
