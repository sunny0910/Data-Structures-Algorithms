def check_balance(a):
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
