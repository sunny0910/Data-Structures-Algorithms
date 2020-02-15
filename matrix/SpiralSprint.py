def matrix_spiral_form(a):
    top = 0
    bottom = len(a)
    left = 0
    right = len(a[0])
    while top < bottom and left < right:
        
        for i in range(left, right):
            print(a[top][i], end=" ")
        top += 1

        for i in range(top, bottom):
            print(a[i][right-1], end=" ")
        right -= 1

        for i in range(right-1, left, -1):
            print(a[bottom-1][i], end=" ")
        bottom -= 1

        for i in range(bottom-1, top, -1):
            print(a[i][left], end=" ")
        left += 1


a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
matrix_spiral_form(a)
