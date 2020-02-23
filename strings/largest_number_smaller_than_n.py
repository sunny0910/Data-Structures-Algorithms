def largestNumberSmallerThanN(n):
    """
    Function to get largest number smaller than N with same set of digits
    :param n: Int
    :return: Int
    """
    n = [int(d) for d in str(n)]
    possible = False
    for i in range(len(n)-1, 0, -1):
        if n[i-1] > n[i]:
            possible = True
            break
    if not possible:
        return -1
    largest_index = i
    for j in range(i, len(n)):
        if n[i-1] > n[j] > n[largest_index]:
            largest_index = j
    n[largest_index], n[i-1] = n[i-1], n[largest_index]
    n1 = n[:i]
    n2 = n[i:]
    n2.sort(reverse=True)
    n = n1+n2
    return int("".join(map(str,n)))

n = 262345
print(n)
print(largestNumberSmallerThanN(n))