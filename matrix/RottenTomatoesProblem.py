def get_time_to_rot(a):
    rot_queue = []
    time = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 2:
                rot_queue.append((i, j))
    if not rot_queue:
        return -1
    rot_queue.append((-1, -1))
    while rot_queue:
        tomatoes_found = False
        while True:
            i, j, = rot_queue.pop(0)
            if i == -1 and j == -1:
                break
            if is_valid_tomato(a, i-1, j):
                rot_queue.append((i-1, j))
                a[i-1][j] = 2
                tomatoes_found = True
            if is_valid_tomato(a, i+1, j):
                rot_queue.append((i+1, j))
                a[i+1][j] = 2
                tomatoes_found = True
            if is_valid_tomato(a, i, j-1):
                rot_queue.append((i, j-1))
                a[i][j-1] = 2
                tomatoes_found = True
            if is_valid_tomato(a, i, j+1):
                rot_queue.append((i, j+1))
                a[i][j+1] = 2
                tomatoes_found = True
        if rot_queue:
            rot_queue.append((-1, -1))
        if tomatoes_found:
            time += 1
    if is_rotten(a):
        return time
    return -1


def is_rotten(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                return False
    return True


def is_valid_tomato(a, i, j):
    if len(a) > i >= 0 and len(a[0]) > j >= 0 and a[i][j] == 1:
        return True
    return False


a = [
    [2, 1, 0, 2, 1],
    [1, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]
]
"""
0: Empty Cell
1: Cells with fresh oranges
2: Cells with rotten oranges
"""
print(get_time_to_rot(a))
