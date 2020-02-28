from heapq import *

"""
Run this file in terminal by providing the elements of stream in stdin
"""


def median_in_stream():
    """
    Function to print median in a running stream.
    It uses max heap on the left side, min heap on the right side and median value in the middle
    Median value will be the average of values at root of heap if both heaps have same number of elements,
    root of max heap if left heap has more number of elements than right heap,
    root of min heap if right heap has more number of elements than left heap.
    :return:None
    """
    def get_weighing_factor(maxheap, minheap):
        """
        Function to get weighing factor of the heaps.
        1 - If left max heap has more elements than right heap
        0 - If both heaps are equal
        -1 - If right min heap has more elements than left heao
        :param maxheap: List
        :param minheap: List
        :return: Int
        """
        if len(maxheap) > len(minheap):
            return 1
        elif len(maxheap) == len(minheap):
            return 0
        else:
            return -1

    maxheap = []
    minheap = []
    median = 0
    while True:
        print("Enter your element in the stream")
        element = int(input())
        weight = get_weighing_factor(maxheap, minheap)
        if weight == 1:
            if element > median:
                heappush(minheap, element)
            else:
                heappush(minheap, -1*heappop(maxheap))
                heappush(maxheap, element*-1)
            median = (maxheap[0]*-1 + minheap[0]) // 2
        elif weight == 0:
            if element > median:
                heappush(minheap, element)
                median = minheap[0]
            else:
                heappush(maxheap, element*-1)
                median = maxheap[0]*-1
        else:
            if element > median:
                x = heapreplace(minheap, element)
                heappush(maxheap, x*-1)
            else:
                heappush(maxheap, element*-1)
            median = (maxheap[0]*-1 + minheap[0]) // 2
        print(median)
