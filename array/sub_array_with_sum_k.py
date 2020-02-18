def subarray_with_sum_k(a, k):
    """
    Function to find sub array with sum k.
    It uses sliding window problem
    :param a: List
    :param k: Int
    :return: Int
    """
    start = end = 0
    total = a[0]
    while start < len(a):
        if total == k:
            return start, end
        if total < k:
            start += 1
            if start+1 < len(a):
                total += a[start]
        else:
            while total > k:
                total -= a[end]
                end += 1
    return -1


a = [1, 4, 20, 3, 10, 5]
k = 7
print(subarray_with_sum_k(a, k))
