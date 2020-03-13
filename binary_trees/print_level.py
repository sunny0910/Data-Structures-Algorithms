from binary_trees.binary_search_tree import BinarySearchTree


def print_level(root, level, ltr):
    """
    Recursive function to print all nodes in one level.
    Used in spiral and zigzak traversal of trees.
    :param root: Node
    :param level: Int
    :param ltr: Bool
    :return: None
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    if ltr:
        print_level(root.left, level-1, ltr)
        print_level(root.right, level-1, ltr)
    else:
        print_level(root.right, level-1, ltr)
        print_level(root.left, level-1, ltr)


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

    print_level(bst.root, 3, True)
