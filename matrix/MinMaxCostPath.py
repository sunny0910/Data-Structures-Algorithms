from sys import maxsize


def is_valid(a, i, j):
    if i < 0 or j < 0 or i > len(a)-1 or j > len(a[0])-1:
        return False
    return True


def get_max_path(a):
    def recur(i, j, total):
        if i == len(a)-1:
            return total
        sum1 = sum2 = sum3 = 0
        if is_valid(a, i+1, j-1):
            sum1 = recur(i+1, j-1, total+a[i+1][j-1])
        if is_valid(a, i+1, j):
            sum2 = recur(i+1, j, total+a[i+1][j])
        if is_valid(a, i+1, j+1):
            sum3 = recur(i+1, j+1, total+a[i+1][j+1])
        return max(sum1, sum2, sum3)
    max_sum = 0
    for i in range(len(a[0])):
        max_sum = max(max_sum, recur(0, i, a[0][i]))
    return max_sum


def get_min_path(a):
    def recur(i, j, total):
        if i == len(a)-1:
            return total
        sum1 = sum2 = sum3 = maxsize
        if is_valid(a, i+1, j-1):
            sum1 = recur(i+1, j-1, total+a[i+1][j-1])
        if is_valid(a, i+1, j):
            sum2 = recur(i+1, j, total+a[i+1][j])
        if is_valid(a, i+1, j+1):
            sum3 = recur(i+1, j+1, total+a[i+1][j+1])
        return min(sum1, sum2, sum3)
    min_sum = maxsize
    for i in range(len(a[0])):
        min_sum = min(min_sum, recur(0, i, a[0][i]))
    return min_sum


a = [
    [10, 10,  2,  0, 20,  4],
    [1,  0,  0, 30,  2,  5],
    [0, 10,  4,  0,  2,  0],
    [1,  0,  2, 20,  1,  4]
]
print(get_max_path(a))
print(get_min_path(a))
