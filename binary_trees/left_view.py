from binary_trees.binary_search_tree import BinarySearchTree


def left_view(root):
    """
    Function to print the left view of a Binary Tree.
    It uses left_view_util function to recursively call and print the left view of the tree
    :param root: Node
    :return: None
    """

    def left_view_util(root, max_level, level):
        """
        Recursive function to print the left view of the binary tree
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
        left_view_util(root.left, max_level, level+1)
        left_view_util(root.right, max_level, level+1)

    max_level = [0]  # max_level in list to pass the parameter by reference in recursive calls
    left_view_util(root, max_level, 1)


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
    
    left_view(bst.root)
