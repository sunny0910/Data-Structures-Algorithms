# pattern matching
def wildcardMatching(string, pattern):
    if string == '' and (pattern == '*' or pattern == ''):
        return True
    print(string, pattern)
    sLength, pLength = len(string), len(pattern)
    dp = [[False for _ in range(sLength)] for _ in range(pLength)]
    if pattern[0] == '*':
        dp[0] = [True for _ in range(sLength)]
    elif pattern[0] == string[0]:
        dp[0][0] = True
    for x in range(1, pLength):
        if pattern[x] == '*' \
                or (pattern[x - 1] == '*' and pattern[x] == string[0]):
            dp[x][0] = dp[x - 1][0]
    for x in range(1, pLength):
        for y in range(1, sLength):
            if pattern[x] == '*':
                dp[x][y] = dp[x - 1][y] or dp[x][y - 1]
            elif pattern[x] == string[y]:
                dp[x][y] = dp[x - 1][y - 1]
    return dp[-1][-1]

assert wildcardMatching("", "") == True
assert wildcardMatching("", "*") == True
assert wildcardMatching("", "ca*t") == False
assert wildcardMatching("catat", "ca*t") == True
assert wildcardMatching("cat", "cat*cat") == False
assert wildcardMatching("cat", "*t") == True
assert wildcardMatching("aaaaaaaabbbbbbbbbbbbcccccccc", "a*b*c") == True