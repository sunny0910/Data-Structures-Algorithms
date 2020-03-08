class Node:
    """
    Class for one node of a tree.
    """
    def __init__(self, value):
        """
        Node with three attributes: left pointer, right pointer and data
        :param value: int
        """
        self.left = None
        self.right = None
        self.data = value
