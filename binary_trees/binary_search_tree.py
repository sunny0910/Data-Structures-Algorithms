from btree_node import Node
from depth_first_search_traversals import in_order
from breadth_first_search_traversal import level_order_using_queue


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        """
        Function to insert into BTree
        :param root: Node
        :param value: Int
        :return: root
        """
        if not root:
            return Node(value)
        if value < root.data:
            root.left = self.insert(root.left, value)
        if value > root.data:
            root.right = self.insert(root.right, value)
        return root

    def delete(self, root, value):
        """
        Function to delete a node in BTree.
        :param root: Node
        :param value: Int
        :return: root
        """
        if not root:
            return
        if value < root.data:
            root.left = self.delete(root.left, value)
            return root
        if value > root.data:
            root.right = self.delete(root.right, value)
            return root
        if not root.left:
            temp = root.right
            return temp
        if not root.right:
            temp = root.left
            return temp
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = self.delete(root.right, temp.data)
        return root


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
    print()
    level_order_using_queue(bst.root)