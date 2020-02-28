from heapq import *


def merge_k_sorted_arrays(matrix, k):
    """
    Function to merge K sorted arrays. A 2-dimensional array will have k arrays in sorted order.
    We will create a Min heap of first element of all the arrays and the node of heaps will have index and k value.
    This way we are creating priority heap where one node has data other than main value used for heaps.
    We will remove minimum value from the heap and insert the next value of the row belonging to the removed value.
    :param matrix: List #2-d list of k sorted lists
    :param k: Int
    :return: List #sorted 1-d list
    """
    op = []
    minheap = []
    for row in range(k):
        node = (matrix[row][0], row, 0)
        minheap.append(node)
    heapify(minheap)
    while minheap:
        min_element = heappop(minheap)
        op.append(min_element[0])
        row, column = min_element[1], min_element[2]
        if column+1 < len(matrix[row]):
            heappush(minheap, (matrix[row][column + 1], row, column + 1))
    return op


a = [[1, 3],
    [2, 4, 6],
    [0, 9, 10, 11]]
n = 3
x = merge_k_sorted_arrays(a, n)
print(x)
