from binary_trees.binary_search_tree import BinarySearchTree


def diff_sum_levels(root):
    """
    Function to calculate the difference between sum of nodes at even level and odd level.
    The function uses level order traversal with two queues to traverse odd and even levels.
    :param root: Node
    :return: Int
    """
    current_level = [root]
    next_level = []
    even_sum = 0
    odd_sum = 0
    odd_level = True
    while current_level:
        node = current_level.pop(-1)
        if odd_level:
            odd_sum += node.data
        else:
            even_sum += node.data
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
        if not current_level:
            current_level, next_level = next_level, current_level
            odd_level = not odd_level
    return odd_sum - even_sum


def diff_sum_levels_recur(root):
    """
    Recursive function to calculate the difference in sum of odd levels and event levels of a binary tree.
    :param root: Node
    :return: Int
    """
    if not root:
        return 0
    return root.data - diff_sum_levels_recur(root.left) - diff_sum_levels_recur(root.right)


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
    sum_diff = diff_sum_levels_recur(bst.root)
    print(sum_diff)
