def max_min_form(a):
    """
    Function to transform an array in alternate maximum minimum form
    :param a: List
    :return: List
    """
    i = 0
    j = len(a)-1
    while i < j:
        last = a.pop()
        a.insert(i, last)
        i += 2
    return a


def max_min_form2(a):
    """
    Second approach to transform element in maximum minimum form
    :param a: List
    :return: Int
    """
    i = 0
    j = len(a)-1
    temp = [0]*len(a)
    flag = True
    for k in range(len(a)):
        if flag:
            temp[k] = a[j]
            j -= 1
        else:
            temp[k] = a[i]
            i += 1
        flag = not flag
    return temp


a = [1, 2, 3, 4, 5, 6, 7]
a = max_min_form2(a)
print(a)