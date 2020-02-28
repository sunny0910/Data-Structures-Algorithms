from heapq import *


def kth_max_using_max_heap(array, k):
    """
    To find the kth maximum value in an array using Max Heaps.
    In this approach, we create a max heap with all the elements in the array and remove the k elements from the heap.
    Kth element to be removed in the Kth maximum value in the array.
    :param array: List
    :param k: Int
    :return: Int #Kth maximum value
    """
    max_heap = list(map(lambda x: x * -1, array))
    ele = None
    heapify(max_heap)
    for i in range(k):
        ele = heappop(max_heap) * -1
    return ele


def kth_max_using_min_heap(array, k):
    """
    To find the Kth maximum value in an array using Min Heaps.
    In this approach, we create a min heap with first K elements of the array.
    After creating the heap, we process the next elements in a way where if element is greater than root of heap(Min
    element in heap) we remove the top and insert the new element.
    This way heap will always have the K maximum elements in the heap and root will always be Kth maximum value
    :param array: List
    :param k: Int
    :return: Int #Kth maximum value
    """
    min_heap = array[:k]
    heapify(min_heap)
    for i in range(k, len(array)):
        if array[i] > min_heap[0]:
            heapreplace(min_heap, array[i])
    return min_heap[0]


a = [10, 90, 10, 5, 20, 30, 15]
k = 3
x = kth_max_using_max_heap(a, k)
print(x)
y = kth_max_using_min_heap(a, k)
print(y)
