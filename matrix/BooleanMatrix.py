def boolean_matrix(a):
    row_one = col_one = False
    for i in range(len(a[0])):
        if a[0][i] == 1:
            row_one = True
    for i in range(len(a)):
        if a[i][0] == 1:
            col_one = True
    for i in range(1, len(a)):
        for j in range(1, len(a[0])):
            if a[i][j] == 1:
                a[i][0] = 1
                a[0][j] = 1
    for i in range(1, len(a)):
        for j in range(1, len(a[0])):
            if a[i][0] == 1 or a[0][j] == 1:
                a[i][j] = 1
    
    if row_one:
        for i in range(len(a[0])):
            a[0][i] = 1
    
    if col_one:
        for i in range(len(a)):
            a[i][0] = 1
    return a


a = [
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]
print(a)
a = boolean_matrix(a)
print(a)
