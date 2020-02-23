def lps(a, i, j):
    if not a:
        return -1
    if i == j:
        return 1
    if a[i] == a[j] and j == i+1:
        return 2
    if a[i] == a[j]:
        return 2 + lps(a, i+1, j-1)
    else:
        return max(lps(a, i, j-1), lps(a, i+1, j))


def lps_op(a):
    n = len(a)
    answers = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        answers[i][i] = 1
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if a[i] == a[j] and cl == 2:
                answers[i][j] = 2
            elif a[i] == a[j]:
                answers[i][j] = 2 + answers[i+1][j-1]
            else:
                answers[i][j] = max(answers[i][j-1], answers[i+1][j])
    return answers[0][n-1]


s = "GEEKSFORGEEKS"
x = lps(s, 0, len(s)-1)
x = lps_op(s)
print(x)