from binary_trees.binary_search_tree import BinarySearchTree


def path_to_node(root, x, path):
    """
    Function to return the path of the target node from root.
    :param root: Node
    :param x: Int #target node
    :param path: List #path from node
    :return: Bool
    """
    if not root:
        return False
    if root.data == x:
        path.append(root.data)
        return True
    if path_to_node(root.left, x, path):
        path.append(root.data)
        return True
    if path_to_node(root.right, x, path):
        path.append(root.data)
        return True
    return False


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
    path = []
    x = 10
    path_to_node(bst.root, x, path)
    path = path[::-1]
    print(path)
