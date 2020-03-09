from binary_trees.binary_search_tree import BinarySearchTree
from binary_trees.height_of_btree import height
from binary_trees.print_level import print_level


def spiral(root, clockwise):
    """
    Function to print the spiral traversal of a binary tree.
    As top and bottom levels are used directly, all the levels are traversed again.
    :param root: Node
    :param clockwise: Bool #direction of traversal
    :return: None
    """
    up = 1
    bottom = height(root)
    ltr = clockwise
    while up < bottom:
        print_level(root, up, ltr)
        up += 1
        print_level(root, bottom, not ltr)
        bottom -= 1
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
    spiral(bst.root, True)
    spiral(bst.root, False)
    