from binary_trees.binary_search_tree import BinarySearchTree


def bottom_right_view(root):
    """
    Function to print the bottom right view of a binary tree.
    Bottom right view is the combination of bottom and right view.
    :param root: Node
    :return: None
    """

    def bottom_right_view_util(root, max_level, level):
        """
        Recursive function to traverse right sub-tree followed with left sub-tree
        and print the nodes with maximum level
        :param root: Node
        :param max_level: List
        :param level: Int
        :return: None
        """
        if not root:
            return
        bottom_right_view_util(root.right, max_level, level+1)
        if level > max_level[0]:
            print(root.data, end=" ")
            max_level[0] = level
        bottom_right_view_util(root.left, max_level, level+1)

    max_level = [0]
    bottom_right_view_util(root, max_level, 1)


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
    bottom_right_view(bst.root)
