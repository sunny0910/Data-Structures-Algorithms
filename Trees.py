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

def in_order(root):
    """
    Inorder traversal of Tree
    :param root: Node
    :return: None
    """
    if not root:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)

def iterative_in_order(root):
    """
    Iterative inorder traversal of a tree using stack.
    :param root: Node
    :return: None
    """
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            node = stack.pop()
            print(node.data, end=" ")
            current = node.right
        else:
            break

def pre_order(root):
    """
    PreOrder traversal of Tree
    :param root: Node
    :return: None
    """
    if not root:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    """
    PostOrder traversal of Tree
    :param root: Node
    :return: None
    """
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=" ")

def level_order_using_queue(root):
    """
    Level order or BFS traversal of a Tree using queue.
    Using queue reduces the time complexity to O(n)
    :param root: Node
    :return: None
    """
    if not root:
        return
    q = []
    q.append(root)
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
def level(root):
    if not root:
        return 0
    left = level(root.left) + 1
    right = level(root.right) + 1
    return max(left, right)

def insert(root, value):
    """
    Function to insert into BTree
    :param root: Node
    :param value: Int
    :return: root
    """
    if not root:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    if value > root.data:
        root.right = insert(root.right, value)
    return root

def delete(root, value):
    """
    Function to delete a node in BTree.
    :param root: Node
    :param value: Int
    :return: root
    """
    if not root:
        return
    if value < root.data:
        root.left = delete(root.left, value)
        return root
    if value > root.data:
        root.right = delete(root.right, value)
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
    root.right = delete(root.right, temp.data)
    return root

def countLeafNodes(root):
    """
    Function to count the number of leaf nodes in a BTree
    :param root: Node
    :return: Int
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return countLeafNodes(root.left) + countLeafNodes(root.right)

def countInternalNodes(root):
    """
    Function to count the number of internal nodes in a BTree
    :param root: Node
    :return: Int
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    return 1 + countInternalNodes(root.left) + countInternalNodes(root.right)

def leftView(root):
    """
    Function to print the left view of a Binary Tree.
    It uses left_view_util function to recursively call and print the left view of the tree
    :param root: Node
    :return: None
    """
    def left_view_util(root, max_level, level):
        """
        Recursive function to print the left view of the binary tree
        :param root: Node
        :param max_level: List
        :param level: Int
        :return: None
        """
        if not root:
            return
        if level > max_level[0]:
            max_level[0] = level
            print(root.data, end=" ")
        left_view_util(root.left, max_level, level+1)
        left_view_util(root.right, max_level, level+1)

    max_level = [0] #max_level in list to pass the parameter by reference in recursive calls
    left_view_util(root, max_level, 1)

def rightViewUtil(root):
    """
    Function to print the right view of a Binary Tree.
    It uses left_view_util function to recursively call and print the right view of the tree.
    :param root: Node
    :return: None
    """
    def rightView(root, max_level, level):
        """
        Recursive function to print the right view of the binary tree.
        :param root: Node
        :param max_level: List
        :param level: Int
        :return: None
        """
        if not root:
            return
        if level > max_level[0]:
            max_level[0] = level
            print(root.data, end=" ")
        rightView(root.right, max_level, level+1)
        rightView(root.left, max_level, level+1)

    max_level = [0]
    rightView(root, max_level, 1)

def topView(root):
    """
    Function to print Top View of the binary tree.
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
        if hd not in hd_map: # Comment this to get bottom view
            hd_map[hd] = node.data
        if node.left:
            node.left.hd = hd-1
            q.append(node.left)
        if node.right:
            node.right.hd = hd+1
            q.append(node.right)
    for hd in sorted(hd_map):
        print(hd_map[hd], end=" ")

def boundaryLeaves(root):
    """
    Function to print the boundary nodes of a Binary Tree.
    This approach will first print the root node and then left boundary nodes except the
    lowest node (as it get's printed in bottom nodes) and then bottom nodes and then right nodes till the left node of root.
    :param root: Node
    :return: None
    """
    def bottom_nodes(node):
        if not node:
            return
        bottom_nodes(node.left)
        if not node.left and not node.right:
            print(node.data, end=" ")
        bottom_nodes(node.right)
    def left_nodes(node):
        if node:
            if node.left:
                print(node.data, end=" ")
                left_nodes(node.left)
            elif node.right:
                print(node.right, end=" ")
                left_nodes(node.right)
    def right_nodes(node):
        if node:
            if node.right:
                right_nodes(node.right)
                print(node.data, end=" ")
            elif node.left:
                right_nodes(node.left)
                print(node.data, end=" ")
    print(root.data, end=" ")
    left_nodes(root.left)
    bottom_nodes(root)
    right_nodes(root.right)

def bottom_right_view(root):
    """
    Function to print the bottom right view of a binary tree.
    Bottom right view is the combination of bottom and right view.
    :param root: Node
    :return: None
    """
    def bottom_right_view_util(root, max_level, level):
        """
        Recursive function to traverse right sub-tree followed with left sub-tree
        and print the nodes with maximum level
        :param root: Node
        :param max_level: List
        :param level: Int
        :return: None
        """
        if not root:
            return
        bottom_right_view_util(root.right, max_level, level+1)
        if level > max_level[0]:
            print(root.data, end=" ")
            max_level[0] = level
        bottom_right_view_util(root.left, max_level, level+1)

    max_level = [0]
    bottom_right_view_util(root, max_level, 1)

def print_level(root, level, ltr):
    """
    Recursive function to print all nodes in one level.
    Used in spiral and zigzak traversal of trees.
    :param root: Node
    :param level: Int
    :param ltr: Bool
    :return: None
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    if ltr:
        print_level(root.left, level-1, ltr)
        print_level(root.right, level-1, ltr)
    else:
        print_level(root.right, level-1, ltr)
        print_level(root.left, level-1, ltr)

def spiral(root, clockwise):
    """
    Function to print the spiral traversal of a binary tree.
    As top and bottom levels are used directly, all the levels are traversed again.
    :param root: Node
    :param clockwise: Bool #direction of traversal
    :return: None
    """
    up = 1
    bottom = level(root)
    ltr = clockwise
    while up<bottom:
        print_level(root, up, ltr)
        up += 1
        print_level(root, bottom, not ltr)
        bottom -= 1

def zigzag(root, clockwise):
    """
    Function to print the zig-zak traversal of a binary tree.
    This function prints new levels by traversing the tree again and again, hence it's not a optimal approach.
    :param root: Node
    :param clockwise: Bool #direction of traversal
    :return: None
    """
    ltr = clockwise
    for i in range(1, level(root)+1):
        print_level(root, i, ltr)
        ltr = not ltr

def zigzak_using_bfs(root):
    """
    Function to print the zig-zak traversal of a binary tree.
    The function uses two queues to store the nodes at current level and nodes at next level.
    If the current level nodes are empty it swaps the current level and next level arrays.
    The direction of zig-zak traversal can be changed by using a boolean parameter to decide the insertion
    of left node or right node into the next level array.
    :param root: Node
    :return: None
    """
    current_level = [root]
    next_level = []
    while current_level:
        node = current_level.pop(-1)
        print(node.data, end=" ")
        if node.right:
            next_level.append(node.right)
        if node.left:
            next_level.append(node.left)
        if not current_level:
            current_level, next_level = next_level, current_level

def nodes_at_k(root, target, k):
    """
    Function to print nodes at distance K from the target node.
    print_k_down is used to print the nodes at distance k from root.
    Function first searches the target node recursively and print the below nodes at distance k.
    If the target node is found in sub-tree, print_k_down in used from parent node to print the root or nodes in left sub-tree.
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

def valid_bst(root, left=None, right=None):
    """
    Recursive function to check whether tree is a valid binary search tree or not.
    :param root: Node
    :param left: Node
    :param right: Node
    :return: Bool
    """
    if not root:
        return True
    if left and left.data > root.data or right and right.data < root.data:
        return False
    return valid_bst(root.left, left, root) and valid_bst(root.right, root, right)

def node_path(root, x, path):
    """
    Function to return the path of the target node from root.
    :param root: Node
    :param x: Int #target node
    :param path: List #path from node
    :return: Bool
    """
    if not root:
        return False
    if root.data == x:
        path.append(root.data)
        return True
    if node_path(root.left, x, path):
        path.append(root.data)
        return True
    if node_path(root.right, x, path):
        path.append(root.data)
        return True
    return False

def lcs(root, a, b):
    """
    Function to find the lowest common ancestor of two nodes.
    Two nodes will always have a common ancestor in a Bianry Tree.
    :param root: Node
    :param a: Node #target node 1
    :param b: Node #target node 2
    :return: Int #LCS value
    """
    if not root:
        return
    path1 = []
    path2 = []
    node_path(root, a, path1)
    node_path(root, b, path2)
    i = len(path1)-1 
    j = len(path2) -1
    while path1[i] == path2[j]:
        i -= 1
        j -= 1
    return path1[i+1]

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
    return (odd_sum - even_sum)

def diff_sum_levels_recur(root):
    """
    Recursive function to calculate the difference in sum of odd levels and event levels of a binary tree.
    :param root: Node
    :return: Int
    """
    if not root:
        return 0
    return root.data - diff_sum_levels_recur(root.left) - diff_sum_levels_recur(root.right)

def is_sum_tree(root):
    """
    Function to check whether the tree is a sum tree or not
    :param root: Node
    :return: Bool
    """

    def get_sum(root):
        """
        Utility function to get the sum of the tree starting from the given root recursively.
        :param root: Node
        :return: Int
        """
        if not root:
            return 0
        return root.data + get_sum(root.left) + get_sum(root.right)

    if not root:
        return True
    l_sum = get_sum(root.left)
    r_sum = get_sum(root.right)
    if (root.left or root.right) and root.data != (l_sum+r_sum):
        return False
    return True

def distance_between_nodes(root, a, b):
    """
    Function to calculate the distance between two target nodes.
    Distance is the number of lines covered in the traversal till that node.
    :param root: Node
    :param a: Int #target node 1
    :param b: Int #target node 2
    :return: Int #distance
    """
    path1 = []
    node_path(root, a, path1)
    path2 = []
    node_path(root, b, path2)
    if not path1 or not path2:
        return 0
    i = len(path1) - 1
    j = len(path2) - 1
    while path1[i] == path2[j]:
        i -= 1
        j -= 1
        if i<0 or j<0:
            return None
    return i+1 + j+1

def check_mirror_trees(root1, root2):
    """
    Recursive function to check if the provided two trees are mirrors of each other.
    :param root1: Node
    :param root2: Node
    :return: Bool
    """
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    return check_mirror_trees(root1.left, root2.right) and check_mirror_trees(root2.left, root1.right)

def check_mirror(root):
    """
    Function to check if a tree is a symmetric tree(mirror of itself).
    It considers the left sub-tree and right sub-tree as independent tree and apply logic of checking if two trees are
    mirror of each other
    :param root: Node
    :return: Bool
    """
    return check_mirror_trees(root.left, root.right)

def create_mirror(root):
    """
    Function to change a tree to its mirror tree.
    This function changes the tree in-place by replacing the left sub-tree with right sub-tree recursively.
    :param root: Node
    :return: None
    """
    if not root:
        return
    create_mirror(root.left)
    create_mirror(root.right)
    if not root.left and not root.right:
        return
    root.left, root.right = root.right, root.left

def max_width(root):
    """
    Function to calculate width of a binary tree.
    Width is the maximum number of nodes at any level in a binary tree.
    This approach uses level order traversal and return maximum length of levels in a tree.
    :param root: Node
    :return: Int
    """
    current_level = [root]
    next_level = []
    max_width = len(current_level)
    while current_level:
        node = current_level.pop()
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
        if not current_level:
            if len(next_level) > max_width:
                max_width = len(next_level)
            current_level, next_level = next_level, current_level
    return max_width

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

def binary_tree_to_dll(root, ll):
    """
    Approach #1 to convert a binary tree to doubly linked list.
    In this approach, a head pointer of linked list is maintained to insert nodes in the linked list.
    While doing in-order traversal of the tree with right sub-tree first and then left sub-tree, every node is
    visited and inserted into the linked list.
    This way rightmost element will be inserted first and leftmost element last and nodes will be inserted in the linked
    list in reverse in-order fashion.
    The head will be present at last inserted node hence linked list will be in-order.
    :param root: Node
    :param ll: LinkedList
    :return: None
    """
    if not root:
        return
    binary_tree_to_dll(root.right, ll)
    if ll.head:
        ll.head.left = root
        root.right = ll.head
    ll.head = root
    binary_tree_to_dll(root.left, ll)

def btree_to_dll(root):
    """
    Approach #2 to convert a binary tree to doubly linked list.
    In this approach, a recursive function is used to convert the binary tree to doubly linked list and
    the leftmost node is searched and returned as the head pointer of LinkedList.
    :param root: Node
    :return: Node #linkedlist head
    """
    def btree_to_dll_util(root):
        """
        Recursive function to traverse every node and find the left and right node of it and make the left and right
        pointers to make it a doubly linked list.
        :param root: Node
        :return: Node
        """
        if not root:
            return
        if root.left:
            left = btree_to_dll_util(root.left)
            while left.right:
                left = left.right
            left.right = root
            root.left = left
        if root.right:
            right = btree_to_dll(root.right)
            while right.left:
                right = right.left
            right.left = root
            root.right = right
        return root
    if not root:
        return
    root = btree_to_dll_util(root)
    while root.left:
        root = root.left
    return root

def print_linkedlist(head):
    """
    Function to print every ndoe in linked list
    :param head: Linkedlist.head
    :return: None
    """
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.right
    print()

class LinkedList:
    """
    Linked list class with head pointer
    """
    def __init__(self):
        self.head = None

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
        if in_start>in_end:
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


root = Node(20) 
root.left = Node(8) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
root.right = Node(22) 
root.right.right = Node(25)

level_order_using_queue(root)
ll = LinkedList()
binary_tree_to_dll(root, ll)
print_linkedlist(ll.head)
inorder = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1]
root = tree_from_inorder_postorder(inorder, postorder)
level_order_using_queue(root)
in_order(root)
print()
inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
root = tree_from_inorder_preorder(inorder, preorder)
level_order_using_queue(root)
in_order(root)