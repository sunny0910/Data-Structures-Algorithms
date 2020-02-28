from heapq import *


def kth_min_using_min_heap(array, k):
    """
    To find the kth minimum value in an array using Min Heaps.
    In this approach, we create a min heap with all the elements in the array and remove the k elements from the heap.
    Kth element to be removed in the Kth minimum value in the array.
    :param array: List
    :param k: Int
    :return: Int #Kth minimum value
    """
    heapify(array)
    ele = None
    for i in range(k):
        ele = heappop(array)
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
    max_heap = array[:k]
    # Workaround of Max Heaps using heapq to multiply the number with -1 to negate the number
    max_heap = list(map(lambda x: x*-1, max_heap))
    heapify(max_heap)
    for i in range(k, len(array)):
        top = max_heap[0] * -1
        if array[i] < top:
            heapreplace(max_heap, array[i] * -1)
    return max_heap[0] * -1

a = [10, 90, 10, 5, 20, 30, 15]
b = [10, 90, 10, 5, 20, 30, 15]
k = 2
x = kth_min_using_max_heap(a, k)
print(x)
y = kth_min_using_min_heap(b, k)
print(y)
