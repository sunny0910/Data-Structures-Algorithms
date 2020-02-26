def lps(a, i, j):
    """
    Function to calculate the length of the longest palindromic sequence in a string.
    This approach takes two pointers on left and and right end of the string and calls the same function recursively
    based on the the condition if character at left and right matches.
    If i == j, which means both are referring to a single character, we return 1 as it's a palindrome.
    If a[i] == a[j], which means both are same characters, we call the function recursively on i+1, j-1 and add two
    to the return of that call.
    If a[i] != a[j], which means characters don't match, we call the function recursively on (i+1, j), (i, j-1) and
    return the maximum value of the two calls.
    :param a: String
    :param i: Int
    :param j: Int
    :return: Int
    """
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
    """
    Optimised approach for the above problem.
    As the above problem has optimal substructure and overlapping sub-problem, it can be solved efficiently using
    dynamic programming approach.
    We maintain a 2-d matrix to calculate the answers and reuse it in other sub-problems.
    :param a: String
    :return: Int
    """
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
