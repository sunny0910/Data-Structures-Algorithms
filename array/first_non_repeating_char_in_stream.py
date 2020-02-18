def first_non_repeating(a):
    """
    Function to get first non-repeating character in a stream.
    It uses count array and returns the first element with count equal to 1
    It traverses the stream twice
    :param a: String
    :return: Int
    """
    count_array = [0] * 256
    for ai in a:
        count_array[ord(ai)] += 1
    for ai in a:
        if count_array[ord(ai)] == 1:
            return ai


def op_first_non_repeating(a):
    """
    This approach modifies the count array to store index as well as count in it.
    This approach traverses the stream once and them traverses the count array to find the non-repeating element
    :param a: String
    :return: Int
    """
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
