def missing_number(a, start, end):
    """
    Function to get the missing number in the array.
    It uses array index and applies binary search to find the missing element
    :param a: List
    :param start: Int
    :param end: Int
    :return: List
    """
    mid = (start+end) // 2
    if (a[mid] - mid) == 2 and (a[mid-1] - (mid-1)) == 1:
        return a[mid]-1
    elif a[mid] - mid == 1:
        return missing_number(a, mid+1, end)
    return missing_number(a, start, mid-1)


a = [1, 2, 3, 4, 6, 7, 8]
x = missing_number(a, 0, len(a))
print(x)
