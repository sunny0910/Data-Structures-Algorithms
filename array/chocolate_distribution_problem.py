def get_lowest_difference(a, m):
    """
    Chocolate distribution problem.
    To get lowest difference between staring and end index of window.
    Uses Window sliding problem to calculate difference between start and end of window
    :param a: List
    :param m: Int
    :return: Int
    """
    a.sort()
    start = m-1
    end = 0
    low_diff = a[start] - a[end]
    while start < len(a):
        if (a[start]-a[end]) < low_diff:
            low_diff = a[start] - a[end]
        start += 1
        end += 1
    return low_diff


a = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
print(get_lowest_difference(a, m))
