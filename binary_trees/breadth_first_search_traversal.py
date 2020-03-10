from binary_trees.binary_search_tree import *
from binary_trees.height_of_btree import height


class BfsTraversal:

    @staticmethod
    def level_order_using_queue(root):
        """
        Level order or BFS traversal of a Tree using queue.
        Using queue reduces the time complexity to O(n)
        :param root: Node
        :return: None
        """
        if not root:
            return
        q = [root]
        while q:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()

    @staticmethod
    def level_order_using_recursion(root):
        """
        Level order or BFS traversal of a Tree using recursion.
        As this traverses the tree again and again for every traversal, the time complexity for this approach is
        relatively higher compared to queue based approach
        :param root:
        :return:
        """

        def print_level(root, level):
            if not root:
                return
            if level == 0:
                print(root.data, end=" ")
            else:
                print_level(root.left, level-1)
                print_level(root.right, level-1)
        for i in range(height(root)):
            print_level(root, i)


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
    BfsTraversal.level_order_using_queue(bst.root)
