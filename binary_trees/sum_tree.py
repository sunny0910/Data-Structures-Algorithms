from binary_trees.binary_search_tree import BinarySearchTree
from binary_trees.btree_node import Node


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
    bst.root = Node(26)
    bst.root.left = Node(10)
    bst.root.right = Node(3)
    bst.root.left.left = Node(4)
    bst.root.left.right = Node(6)
    bst.root.right.right = Node(3)
    """
    Tree representation of above numbers
                26
               /  \
              10    3
             / \     \
            4   6     3
    
    in-order traversal - 4, 8, 10, 12, 14, 20, 22, 25
    """
    x = is_sum_tree(bst.root)
    print("Before adding extra node - ", x)
    bst.root.right.left = Node(2)
    x = is_sum_tree(bst.root)
    print("After added extra node - ", x)
