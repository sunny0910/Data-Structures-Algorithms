def bitonic_point(a, start, end):
    """
    Function to find bitonic point in an array.
    Bitonic array is the array with increases initially and then gradually decreases.
    :param a: List
    :param start: Int
    :param end: Int
    :return: Int
    """
    mid = (start+end) // 2
    if a[mid+1] < a[mid] > a[mid-1]:
        return a[mid]
    elif a[mid+1] > a[mid] > a[mid-1]:
        return bitonic_point(a, mid+1, end)
    else:
        return bitonic_point(a, start, end-1)


a = [5, 6, 7, 8, 9, 10, 3, 2, 1]
x = bitonic_point(a, 0, len(a))
print(x)
