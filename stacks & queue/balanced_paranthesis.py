def check_balance(a):
    """
    Function to check is parentheses in an expression are balances or not.
    It uses stack to resolve the opening and closing parentheses.
    :param a: String
    :return: Bool
    """
    stack = []
    for ai in a:
        if ai in ('[', '(', '{'):
            stack.append(ai)
        elif ai == ']' and stack[-1] == '[':
            stack.pop(-1)
        elif ai == '}' and stack[-1] == '{':
            stack.pop(-1)
        elif ai == ')' and stack[-1] == '(':
            stack.pop(-1)
        else:
            stack.append(ai)
        print(stack)
    print(stack)
    if stack:
        return False
    return True
        

a = "[(])"
print(check_balance(a))
