def path_exits(a):
    if 1 not in a[0]:
        return 'safe'
    q = [[] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                q[i].append((i, j))
    i = 0
    for one_level in q:
        level_result = 0
        for element in one_level:
            i, j = element
            flow = [(i+1, j-1), (i+1, j), (i+1, j+1)]
            if i+1 < len(a) and all(node not in q[i+1] for node in flow):
                level_result += 1
        if level_result == len(one_level):
            return 'safe'
    return 'unsafe'


def path_exists_recur(a):
    def recur(a, i, j):
        if i == len(a)-1 and a[i][j] == 1:
            return True
        if i < 0 or j < 0 or i > len(a)-1 or j > len(a[0])-1 or a[i][j] == 0:
            return False
        return recur(a, i+1, j-1) or recur(a, i+1, j) or recur(a, i+1, j+1)
    q = []
    for index, ai in enumerate(a[0]):
        if ai == 1:
            q.append((0, index))
    for i in q:
        x = recur(a, i[0], i[1])
        if x:
            return 'unsafe'
    return 'safe'


a = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1]
]
print(path_exits(a))
print(path_exists_recur(a))
