
def check_mirror_trees(root1, root2):
    """
    Recursive function to check if the provided two trees are mirrors of each other.
    :param root1: Node
    :param root2: Node
    :return: Bool
    """
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    return check_mirror_trees(root1.left, root2.right) and check_mirror_trees(root2.left, root1.right)


def check_mirror(root):
    """
    Function to check if a tree is a symmetric tree(mirror of itself).
    It considers the left sub-tree and right sub-tree as independent tree and apply logic of checking if two trees are
    mirror of each other
    :param root: Node
    :return: Bool
    """
    return check_mirror_trees(root.left, root.right)


def create_mirror(root):
    """
    Function to change a tree to its mirror tree.
    This function changes the tree in-place by replacing the left sub-tree with right sub-tree recursively.
    :param root: Node
    :return: None
    """
    if not root:
        return
    create_mirror(root.left)
    create_mirror(root.right)
    if not root.left and not root.right:
        return
    root.left, root.right = root.right, root.left


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