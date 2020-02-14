def first_non_repeating(a):
    count_array = [0] * 256
    for ai in a:
        count_array[ord(ai)] += 1
    for ai in a:
        if count_array[ord(ai)] == 1:
            return ai


def op_first_non_repeating(a):
    count_array = [0] * 256
    for index, ai in enumerate(a):
        if count_array[ord(ai)] == 0:
            count_array[ord(ai)] = [1, index]
        else:
            count_array[ord(ai)][0] += 1
    for ele in count_array:
        if ele == 0:
            continue
        count, index = ele[0], ele[1]
        if count == 1:
            return a[index]
    return -1


a = "GeeksforGeeks"
x = op_first_non_repeating(a)
print(x)
