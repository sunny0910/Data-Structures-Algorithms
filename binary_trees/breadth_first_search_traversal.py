
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


def level_order_using_recurssion(root):
    """
    Level order or BFS traversal of a Tree using recursion.
    As this traverses the tree again and again for every traversal, the time complexity for this approach is relatively
    higher compared to queue based approach
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
    for i in range(level(root)):
        print_level(root, i)
