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


if __name__ == "__main__":
    a = [7, 6, 5, 4, 3, 2, 1, 8]
    b = quick_sort(a, 0, len(a)-1)
    print(b)
