def rotate_matrix(a):
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
