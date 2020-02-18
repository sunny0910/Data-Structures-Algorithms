def boolean_matrix(a):
    """
    Function to make all elements in same row and column if element is equal to 1
    It uses the first row and first column to store which rows and columns have element 1 in one traversal.
    And then in next traversal it makes all those rows and columns equal to 1.
    It uses row and column variable to store whether first row and first columns already had 1 or not
    :param a: List # Matrix
    :return: List # Modified Matrix
    """
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
