from binary_trees.binary_search_tree import BinarySearchTree


def nodes_at_k(root, target, k):
    """
    Function to print nodes at distance K from the target node.
    print_k_down is used to print the nodes at distance k from root.
    Function first searches the target node recursively and print the below nodes at distance k.
    If the target node is found in sub-tree, print_k_down in used from parent node to print the root or nodes in left
    sub-tree.
    :param root: Node
    :param target: Int #target node data
    :param k: Int #distance value
    :return: None
    """

    def print_k_down(root, k):
        """
        function to print the nodes below the root node and distance k
        :param root: Node
        :param k: Int #distance
        :return: Nine
        """
        if not root:
            return
        if k == 0:
            print(root.data, end=" ")
        print_k_down(root.left, k-1)
        print_k_down(root.right, k-1)

    if not root:
        return -1
    if target == root.data:
        print_k_down(root, k)
        return 1
    ld = nodes_at_k(root.left, target, k)
    if ld != -1:
        if ld == k:
            print(root.data, end=" ")
        else:
            print_k_down(root.right, k-2)
        return 1+ld
    rd = nodes_at_k(root.right, target, k)
    if rd != -1:
        if rd+2 == k:
            print(root.data, end=" ")
        else:
            print_k_down(root.left, k-2)
        return 1+rd
    return -1


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
    
    nodes_at_k(bst.root, 8, 2)
