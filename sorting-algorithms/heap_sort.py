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


if __name__ == "__main__":
    a = [7, 6, 5, 4, 3, 2, 1, 8]
    x = heap_sort(a)
    print(x)
