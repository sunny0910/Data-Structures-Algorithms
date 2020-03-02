def next_smaller_element(a):
    for i, ai in enumerate(a):
        found = False
        print(a[i], end=" - ")
        for j in range(i, len(a)):
            if a[j] < a[i]:
                print(a[j])
                found = True
                break
        if not found:
            print(-1)

def optimised_next_smaller_element(a):
    stack = []
    op_list = [-1] * len(a)
    i = 0
    while i<len(a):
        while stack and a[i] < stack[-1]:
            x = stack.pop(-1)
            op_list[a.index(x)] = a[i]
        stack.append(a[i])
        i += 1
    i = 0
    while i<len(a):
        print(a[i], " - ", op_list[i])
        i += 1

a = [4, 8, 5, 2, 25]
optimised_next_smaller_element(a)
