from heapq import *

"""
Run this file in terminal by providing the value of K followed by the input element of stream.
"""


def kth_largest_element_in_stream():
    """
    Function to print Kth largest element in a running stream.
    It will use a min heap of size k and will always print the root of the heap.
    If the size of min heap is less than k, it will print -1
    :return: None
    """
    k = int(input())
    min_heap = []
    while 1:
        x = int(input())
        if len(min_heap) < k:
            heappush(min_heap, x)
            print(-1)
            continue
        elif x > min_heap[0]:
            heapreplace(min_heap, x)
        print(min_heap[0])


a = [10, 90, 10, 5, 20, 30, 15]
