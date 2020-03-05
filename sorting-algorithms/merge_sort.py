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


if __name__ == "__main__":
    c = [7, 6, 5, 4, 3, 2, 1, 8]
    a = merge_sort(c)
    print(a)
