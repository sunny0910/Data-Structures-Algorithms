from binary_trees.btree_node import Node
from binary_trees.breadth_first_search_traversal import BfsTraversal
from binary_trees.depth_first_search_traversals import DfsTraversals


def tree_from_inorder_preorder(inorder, preorder):
    """
    Function to create a tree from it's in-order and pre-order traversals.
    It uses a recursive function to create one node at a time and call for it's left and right nodes.
    It uses indexes in in-order array while calling for left and right node
    :param inorder: List
    :param preorder: List
    :return: Node
    """
    if not preorder or not inorder:
        return

    def recur_function(in_start, in_end, p_index):
        """
        Recursive function to create a node and call for it's left and right nodes.
        It uses p_index as a index to pre-order(Root-Left-Right) to create nodes in increasing order as root is
        visited last in pre-order traversal.
        :param in_start: Int
        :param in_end: Int
        :param p_index: Int
        :return: Node
        """
        if in_start > in_end:
            return
        data = preorder[p_index[0]]
        p_index[0] += 1
        node = Node(data)
        if in_start == in_end:
            return node
        in_index = inorder_map[data]
        node.left = recur_function(in_start, in_index-1, p_index)
        node.right = recur_function(in_index+1, in_end, p_index)
        return node

    inorder_map = {data: index for index, data in enumerate(inorder)}
    p_index = [0]
    root = recur_function(0, len(inorder)-1, p_index)
    return root


if __name__ == "__main__":
    inorder = ['D', 'B', 'E', 'A', 'F', 'C']
    preorder = ['A', 'B', 'D', 'E', 'C', 'F']
    """
    Tree representation of above data
                 A
               /  \
              B     C
             / \    /
            D   E  F
    
    level-order traversal - A, B, C, D, E, F
    in-order traversal - D, B, E, A, F, C
    """
    root = tree_from_inorder_preorder(inorder, preorder)
    BfsTraversal.level_order_using_queue(root)
    DfsTraversals.in_order(root)
