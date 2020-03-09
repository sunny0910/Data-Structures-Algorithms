from binary_trees.btree_node import Node
from binary_trees.breadth_first_search_traversal import level_order_using_queue


def tree_from_inorder_postorder(inorder, postorder):
    """
    Function to create a tree from it's in-order and post-order traversals.
    It uses a recursive function to create one node at a time and call for it's left and right nodes.
    It uses indexes in in-order array while calling for left and right node
    :param inorder: List
    :param postorder: List
    :return: Node
    """
    if not postorder or not inorder:
        return

    def recur_function(inorder_start, inorder_end, p_index):
        """
        Recursive function to create a node and call for it's left and right nodes.
        It uses p_index as a index to post-order(Left-Right-Root) to create nodes in reverse order as root is
        visited last in post-order traversal.
        :param inorder_start: Int
        :param inorder_end: Int
        :param p_index: Int
        :return: Node
        """
        if inorder_start > inorder_end:
            return
        data = postorder[p_index[0]]
        p_index[0] -= 1
        node = Node(data)
        if inorder_start == inorder_end:
            return node
        in_index = inorder_map[data]
        node.right = recur_function(in_index+1, inorder_end, p_index)
        node.left = recur_function(inorder_start, in_index-1, p_index)
        return node
    inorder_map = {data: index for index, data in enumerate(inorder)}
    p_index = [len(postorder) - 1]
    root = recur_function(0, len(inorder)-1, p_index)
    return root


if __name__ == "__main__":
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    postorder = [8, 4, 5, 2, 6, 7, 3, 1]
    root = tree_from_inorder_postorder(inorder, postorder)
    level_order_using_queue(root)