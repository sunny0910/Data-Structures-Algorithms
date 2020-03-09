from binary_trees.binary_search_tree import BinarySearchTree
from binary_trees.print_level import print_level
from binary_trees.height_of_btree import height


def zigzak(root, clockwise):
    """
    Function to print the zig-zak traversal of a binary tree.
    This function prints new levels by traversing the tree again and again, hence it's not a optimal approach.
    :param root: Node
    :param clockwise: Bool #direction of traversal
    :return: None
    """
    ltr = clockwise
    for i in range(1, height(root)+1):
        print_level(root, i, ltr)
        ltr = not ltr


def zigzak_using_bfs(root):
    """
    Function to print the zig-zak traversal of a binary tree.
    The function uses two queues to store the nodes at current level and nodes at next level.
    If the current level nodes are empty it swaps the current level and next level arrays.
    The direction of zig-zak traversal can be changed by using a boolean parameter to decide the insertion
    of left node or right node into the next level array.
    :param root: Node
    :return: None
    """
    current_level = [root]
    next_level = []
    while current_level:
        node = current_level.pop(-1)
        print(node.data, end=" ")
        if node.right:
            next_level.append(node.right)
        if node.left:
            next_level.append(node.left)
        if not current_level:
            current_level, next_level = next_level, current_level


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
    zigzak(bst.root, True)