from binary_trees.binary_search_tree import BinarySearchTree


def has_path_sum(root, s):
    """
    Function to check if root to leaf path with path sum equal to provided sum exists
    :param root: Node
    :param s: Int #provided sum
    :return: Bool
    """
    if not root:
        return s == 0
    ans = 0
    sub_sum = s - root.data
    if sub_sum == 0 and not root.left and not root.right:
        return True
    if root.left:
        ans = ans or has_path_sum(root.left, sub_sum)
    if root.right:
        ans = ans or has_path_sum(root.right, sub_sum)
    return ans


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
    
    print(has_path_sum(bst.root, 32)) # 20->8->4 = 32
    print(has_path_sum(bst.root, 67))
