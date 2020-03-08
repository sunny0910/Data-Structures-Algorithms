from binary_trees.binary_search_tree import BinarySearchTree


def boundary_leaves(root):
    """
    Function to print the boundary nodes of a Binary Tree.
    This approach will first print the root node and then left boundary nodes except the
    lowest node (as it get's printed in bottom nodes) and then bottom nodes and then right nodes till the left node of
    the root.
    :param root: Node
    :return: None
    """

    def bottom_nodes(node):
        if not node:
            return
        bottom_nodes(node.left)
        if not node.left and not node.right:
            print(node.data, end=" ")
        bottom_nodes(node.right)

    def left_nodes(node):
        if node:
            if node.left:
                print(node.data, end=" ")
                left_nodes(node.left)
            elif node.right:
                print(node.data, end=" ")
                left_nodes(node.right)

    def right_nodes(node):
        if node:
            if node.right:
                right_nodes(node.right)
                print(node.data, end=" ")
            elif node.left:
                right_nodes(node.left)
                print(node.data, end=" ")
    print(root.data, end=" ")
    left_nodes(root.left)
    bottom_nodes(root)
    right_nodes(root.right)

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
    boundary_leaves(bst.root)