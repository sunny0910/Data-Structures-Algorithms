def merge_sort(input_array):
    """
    Merge sort is an Divide and Conquer algorithm. It divides the input array in two halves, call itself for the two
    halves and then merges the two sorted two halves.
    The time complexity of the merge sort is O(nlogn) in all three cases(Worst, Average, Best)
    The space complexity of the merge sort is O(n) as it requires auxiliary space to store two halves in every call.
    :param input_array: List #Unsorted array
    :return: List #Sorted array
    """
    if len(input_array) > 1:
        n = len(input_array) // 2
        left_half = input_array[:n]
        right_half = input_array[n:]
        merge_sort(left_half)
        merge_sort(right_half)
        left_index = right_index = input_index = 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                input_array[input_index] = left_half[left_index]
                left_index += 1
                input_index += 1
            else:
                input_array[input_index] = right_half[right_index]
                right_index += 1
                input_index += 1
        while left_index < len(left_half):
            input_array[input_index] = left_half[left_index]
            left_index += 1
            input_index += 1
        while right_index < len(right_half):
            input_array[input_index] = right_half[right_index]
            right_index += 1
            input_index += 1
    return input_array

def quick_sort(input_array, start_index, end_index):
    """
    Quick sort is an in-place divide and conquer algorithm. It separates the elements of input array in two halves
    based on the partition(pivot) value. Elements less than pivot value to it's left and greater than pivot value to
    it's right. Partition value can be selected through few ways (First value/Last value/Median value).
    The time complexity of the quick sort is O(nlogn) for best and average case, and O(n^2) for worst case.
    Although the worst case complexity of quick sort is higher compared to merge or heap sort, quick sort can perform
    faster in certain scenarios where pivot strategy is planned as per data so that worst case doesn't occur.
    However, merge sort is generally considered better when data is huge and stored in external storage.
    :param input_array: List #Unsorted array
    :param start_index: Int
    :param end_index: Int
    :return: List #Sorted array
    """
    def partition(array, start, end):
        """
        Partition function to separate the array elements based on the partition value.
        Last value is considered as pivot value here. Elements less than the pivot values are shifted to left and
        elements greater than the pivot value are shifted to right and pivot value is shifted in the middle of the
        left and right values.
        :param array: List
        :param start: Int
        :param end: Int
        :return: Int #Pivot value index
        """
        pivot = array[end]
        j = start - 1
        for i in range(start, end):
            if array[i] < pivot:
                j += 1
                array[j], array[i] = array[i], array[j]
        array[j + 1], array[end] = array[end], array[j + 1]
        return j+1

    if start_index < end_index:
        partition_index = partition(input_array, start_index, end_index)
        quick_sort(input_array, start_index, partition_index - 1)
        quick_sort(input_array, partition_index + 1, end_index)
    return input_array

def heap_sort(input_array):
    """
    Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to
    selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same
    process for remaining element.
    The time complexity of heap sort is O(nlogn)
    :param input_array: List #Unsorted array
    :return: List #Sorted array
    """
    def heapify(array, index, n):
        """
        Heapification algorithm for heap sort.
        Heapify compares the element with it's left and right child elements to check it any of them is
        greater(in Max Heap) or smaller(in Min Heap) than the parent element. Heap sort required Max heap, so max heap
        is implemented below. If any of the element violates the condition, the element is swapped with the parent
        element and heapify is called on that element to recursively check the condition on it's child elements.
        :param array:List #Heap represented in an array
        :param index: Int #Index at which heapify logic is to be applied
        :param n: Int #Size of heap to be considered
        :return: None
        """
        left_child = 2*index + 1
        right_child = 2*index + 2
        largest = index
        if left_child < n and array[left_child] > array[index]:
            array[left_child], array[index] = array[index], array[left_child]
            largest = left_child
        if right_child < n and array[right_child] > array[index]:
            array[right_child], array[index] = array[index], array[right_child]
            largest = right_child
        if largest != index:
            heapify(array, largest, n)

    for i in range(len(input_array) - 1, -1, -1):
        heapify(input_array, i, len(input_array))
    for i in range(len(input_array) - 1, 0, -1):
        input_array[i], input_array[0] = input_array[0], input_array[i]
        heapify(input_array, 0, i)
    return a

a = [7, 6, 5, 4, 3, 2, 1, 8]
b = [7, 6, 5, 4, 3, 2, 1, 8]
c = [7, 6, 5, 4, 3, 2, 1, 8]
a = merge_sort(a)
print(a)
b = quick_sort(b, 0, len(a)-1)
print(b)
c = heap_sort(c)
print(c)