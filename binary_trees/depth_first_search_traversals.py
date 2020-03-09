# from binary_trees.binary_search_tree import BinarySearchTree


def in_order(root):
    """
    Inorder traversal of Tree
    :param root: Node
    :return: None
    """
    if not root:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)


def iterative_in_order(root):
    """
    Iterative inorder traversal of a tree using stack.
    :param root: Node
    :return: None
    """
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            node = stack.pop()
            print(node.data, end=" ")
            current = node.right
        else:
            break
    print()


def pre_order(root):
    """
    PreOrder traversal of Tree
    :param root: Node
    :return: None
    """
    if not root:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)


def post_order(root):
    """
    PostOrder traversal of Tree
    :param root: Node
    :return: None
    """
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=" ")


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
    in_order(bst.root)
    pre_order(bst.root)
    post_order(bst.root)