a = [8, 9, 1, 2, 3, 4, 5, 6, 7]
# a = [4 ,5 ,6, 7, 8, 9, 1, 2, 3]


def find_lowest(a, low, high):
    """
    To find the lowest number in a sorted rotated array.
    The approach is to use binary search recursively and check for condition on the middle element of sub-arrays
    If middle element is not lower than the mid-1 element, then recursive call on either left or right sub-array.
    If a[mid] < a[high] then left sub-array else right sub-array.
    :param a: List
    :param low: Int
    :param high: Int
    :return: Int
    """
    if not a:
        return -1
    if a[0] < a[-1]:
        return a[0]
    if low == high:
        return a[low]
    mid = (low+high) // 2
    if a[mid-1] > a[mid] and a[mid] < a[mid+1]:
        return a[mid]
    elif a[mid] < a[high-1]:
        return find_lowest(a, 0, mid-1)
    else:
        return find_lowest(a, mid+1, high)


x = find_lowest(a, 0, len(a)-1)
print(x)
