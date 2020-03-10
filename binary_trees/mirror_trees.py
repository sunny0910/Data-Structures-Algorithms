from binary_trees.btree_node import Node


def check_mirror(root):
    """
    Function to check if a tree is a symmetric tree(mirror of itself).
    It considers the left sub-tree and right sub-tree as independent tree and apply logic of checking if two trees are
    mirror of each other
    :param root: Node
    :return: Bool
    """
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
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.left.right = Node(4) 
    root.right.left = Node(4) 
    root.right.right = Node(3) 
    """
    Tree representation of above numbers
                1
               / \
              2    2
             / \   / \
            3   4  3  4
    
    in-order traversal - 3, 2, 4, 1, 3, 2, 4
    """
    print(check_mirror(root))
    root.right.right = Node(5)  # Changing one value
    print(check_mirror(root))
