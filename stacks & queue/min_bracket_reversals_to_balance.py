from math import ceil


def minimum_bracket_reversals(a):
    """
    Function to get the minimum bracket reversals required to balance the expression.
    The approach is to balance the exp and count the number of opening brackets and closing brackets.
    The minimum number of reversals will be sum of ceil value of number of opening brackets divide by 2 and number of
    closing bracket divide by 2.
    ceil(opening_count/2) + ceil(closing_count/2)
    :param a: String
    :return: Int
    """
    if not a or len(a) % 2 == 1:
        return -1
    stack = []
    for ai in a:
        if ai == "}" and stack and stack[-1] == "{":
            stack.pop(-1)
            continue
        stack.append(ai)

    opening_count = 0
    closing_count = 0
    for ai in stack:
        if ai == "{":
            opening_count += 1
        elif ai == "}":
            closing_count += 1
    return ceil(opening_count / 2) + ceil(closing_count / 2)


exp = "{{{{"
x = minimum_bracket_reversals(exp)
print(x)
