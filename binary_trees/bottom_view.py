from binary_trees.binary_search_tree import BinarySearchTree


def bottom_view(root):
    """
    Function to print Bottom View of the binary tree.
    It uses python dictionary to store the node's value at various horizontal levels.
    The time complexity of this approach is O(n) where n is number of nodes
    and space complexity of this approach is equal to the width of the binary tree.
    Top view and Bottom view only differ in storing the latest value in the respective level.
    Storing all the updates will give us bottom view, while storing the first node will give us Top View.
    :param root: Node
    :return: None
    """
    root.hd = 0
    q = [root]
    hd_map = {}
    while q:
        node = q.pop(0)
        hd = node.hd
        hd_map[hd] = node.data
        if node.left:
            node.left.hd = hd-1
            q.append(node.left)
        if node.right:
            node.right.hd = hd+1
            q.append(node.right)
    for hd in sorted(hd_map):
        print(hd_map[hd], end=" ")


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
    
    bottom_view(bst.root)
