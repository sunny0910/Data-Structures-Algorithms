def rotate_matrix(a):
    """
    Function to rotate a matrix in-place.
    For every square matrix, the formula for number of matrix is ceil(n/2) and the rotation of elements can be done
    using this where we will use one temporary variable to swap 4 nodes at a time.
    :param a: List # Matrix
    :return: None
    """
    n = len(a)
    x = n//2
    for i in range(x):
        for j in range(i, n-1-i):
            temp = a[i][j]
            a[i][j] = a[j][(n-1)-i]
            a[j][(n-1)-i] = a[(n-1)-i][(n-1)-j]
            a[(n-1)-i][(n-1)-j] = a[(n-1)-j][i]
            a[(n-1)-j][i] = temp


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_matrix(a)
print(a)
