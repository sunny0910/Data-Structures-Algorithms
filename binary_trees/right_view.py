from binary_trees.binary_search_tree import BinarySearchTree


def right_view(root):
    """
    Function to print the right view of a Binary Tree.
    It uses left_view_util function to recursively call and print the right view of the tree.
    :param root: Node
    :return: None
    """

    def right_view(root, max_level, level):
        """
        Recursive function to print the right view of the binary tree.
        :param root: Node
        :param max_level: List
        :param level: Int
        :return: None
        """
        if not root:
            return
        if level > max_level[0]:
            max_level[0] = level
            print(root.data, end=" ")
        right_view(root.right, max_level, level+1)
        right_view(root.left, max_level, level+1)

    max_level = [0]
    right_view(root, max_level, 1)


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
    
    right_view(bst.root)
