def get_max_diff(a):
    """
    Function to get Max Difference between two elements so that the second element occurs after the first element.
    This approach can be used in buy stuck and sell problem where buying and selling only once is allowed.
    It keeps track of the minimum element so far and maximum difference so far.
    It can return the two elements using minimum element and adding the difference to get highest element.
    :param a: List
    :return: Int
    """
    if not a or len(a) == 1:
        return -1
    max_diff = 0
    min_element = a[0]
    for i in range(len(a)):
        if a[i] < min_element:
            min_element = a[i]
        diff = a[i] - min_element
        if diff > max_diff:
            max_diff = diff
    return max_diff


arr = [2, 3, 10, 6, 4, 8, 1]
# arr = [7, 9, 5, 6, 3, 2]
x = get_max_diff(arr)
print(x)
