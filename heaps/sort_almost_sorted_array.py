from heapq import *


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


a = [12, 13, 10, 15, 14, 16]
x = sort_almost_sorted(a, 2)
print(x)
