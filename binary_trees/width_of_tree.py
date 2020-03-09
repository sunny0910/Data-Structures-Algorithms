from binary_trees.binary_search_tree import BinarySearchTree


def max_width(root):
    """
    Function to calculate width of a binary tree.
    Width is the maximum number of nodes at any level in a binary tree.
    This approach uses level order traversal and return maximum length of levels in a tree.
    :param root: Node
    :return: Int
    """
    current_level = [root]
    next_level = []
    max_width = len(current_level)
    while current_level:
        node = current_level.pop()
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
        if not current_level:
            if len(next_level) > max_width:
                max_width = len(next_level)
            current_level, next_level = next_level, current_level
    return max_width


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
    x = max_width(bst.root)
    print(x)
