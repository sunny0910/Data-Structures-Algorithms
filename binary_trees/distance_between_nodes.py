from binary_trees.path_to_node import path_to_node
from binary_trees.binary_search_tree import BinarySearchTree


def distance_between_nodes(root, a, b):
    """
    Function to calculate the distance between two target nodes.
    Distance is the number of lines covered in the traversal till that node.
    :param root: Node
    :param a: Int #target node 1
    :param b: Int #target node 2
    :return: Int #distance
    """
    path1 = []
    path_to_node(root, a, path1)
    path2 = []
    path_to_node(root, b, path2)
    if not path1 or not path2:
        return 0
    i = len(path1) - 1
    j = len(path2) - 1
    while path1[i] == path2[j]:
        i -= 1
        j -= 1
        if i < 0 or j < 0:
            break
    return (i + 1) + (j + 1)


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
    x = distance_between_nodes(bst.root, 8, 14)
    print(x)
