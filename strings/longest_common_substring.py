def lcs(i, j):
    if i == 0 or j == 0:
        return 0
    count = 0
    if a[i-1] == b[j-1]:
        return 1 + lcs(i-1, j-1)
    else:
        return max(count, lcs(i-1, j), lcs(i, j-1))


def lcs_op(x, y, i, j):
    answers = [[0 for columns in range(i+1)] for rows in range(j+1)]

    result = 0

    for m in range(i+1):
        for n in range(j+1):
            if m == 0 or n == 0:
                answers[m][n] = 0
            elif x[m-1] == y[n-1]:
                answers[m][n] = 1 + answers[m-1][n-1]
                result = max(result, answers[m][n])
            else:
                answers[m][n] = 0
    return result

a = "abcdxyz"
b = "xyzabcd"
m = len(a)
n = len(b)
x = lcs(m, n)
x = lcs_op(a, b, m, n)
print(x)