from heapq import *


"""
python library to implement heaps.
It supports Min Heap by default. To implement Max Heap the workaround we're using is to make the number negative while
inserting and removing.
It works for most of the scenarios
"""


def kth_min_using_min_heap(array, k):
    """
    To find the kth minimum value in an array using Min Heaps.
    In this approach, we create a min heap with all the elements in the array and remove the k elements from the heap.
    Kth element to be removed in the Kth minimum value in the array.
    :param array: List
    :param k: Int
    :return: Int #Kth minimum value
    """
    minheap = heapify(array)
    ele = None
    for i in range(k):
        ele = heappop(minheap)
    return ele


def kth_min_using_max_heap(array, k):
    """
    To find the Kth minimum value in an array using Max Heaps.
    In this approach, we create a max heap with first K elements of the array.
    After creating the heap, we process the next elements in a way where if element is less than root of heap(Max
    element in heap) we remove the top and insert the new element.
    This way heap will always have the K minimum elements in the heap and root will always be Kth minimum value
    :param array: List
    :param k: Int
    :return: Int #Kth minimum value
    """
    maxheap = array[:k]
    # Workaround of Max Heaps using heapq to multiply the number with -1 to negate the number
    maxheap = list(map(lambda x: x*-1, maxheap))
    heapify(maxheap)
    for i in range(k, len(array)):
        top = maxheap[0] * -1
        if array[i] < top:
            heapreplace(maxheap, array[i] * -1)
    return maxheap[0] * -1


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
    minheap = array[:k]
    heapify(minheap)
    for i in range(k, len(array)):
        if array[i] > minheap[0]:
            heapreplace(minheap, array[i])
    return minheap[0]


def sort_almost_sorted(array, k):
    """
    Function to sort a almost sorted array.
    Array will have it's elements at least k indexes away.
    We will use min heap for first k+1 elements which will get us our first element in the root of the heap.
    The next elements will be processed by removing the minimum element from heap and inserting the new element.
    This way the removing of elements from the heap will be in increasing order.
    :param array: List #Usorted list
    :param k: Int
    :return: List #Sorted list
    """
    minheap = array[:k + 1]
    heapify(minheap)
    j = 0
    for i in range(k+1, len(array)):
        array[j] = heapreplace(minheap, array[i])
        j += 1
    while minheap:
        array[j] = heappop(minheap)
        j += 1
    return array


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


def kth_largest_element_in_stream(k):
    """
    Function to print Kth largest element in a running stream.
    It will use a min heap of size k and will always print the root of the heap.
    If the size of min heap is less than k, it will print -1
    :param k: Int
    :return: None
    """
    minheap = []
    while 1:
        x = int(input())
        if len(minheap) < k:
            heappush(minheap, x)
            print(-1)
            continue
        elif x > minheap[0]:
            heapreplace(minheap, x)
        print(minheap[0])


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


a = [[1, 3],
    [2, 4, 6],
    [0, 9, 10, 11]]
k = 3
median_in_stream()
