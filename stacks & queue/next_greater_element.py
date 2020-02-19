def next_greater_element(array):
    """
    This approach uses two for loops, one to iterate over every element and second to iterate over subsequent elements
    to find the next greater element.
    The time complexity for this approach is O(n^2)
    :param array: List
    :return: None
    """
    for i in range(len(array)):
        found = False
        print(array[i], end=" - ")
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                found = True
                print(array[j])
                break
        if not found:
            print(-1)


def optimised_next_greater_element(array):
    """
    This approach uses a stack to find the next greater element. It pushes the first element in the stack and
    processes the next elements in a way where if next element is greater than stack top, keep popping the stack top
    until stack top is lower than next element, then push the next element in the stack.
    For all the popped elements, next element is the next greater element and the lastly print -1 for elements
    remaining in the stack as they don't have a next greater element.
    Considering stack pop, push and comparison operations to be O(1), the time complexity of this approach is O(n) as it
    traverses the array only once.
    :param array: List
    :return: None
    """
    stack = []
    op = [-1] * len(array)
    stack.append(array[0])
    for i in range(1, len(array)):
        if array[i] < stack[-1]:
            stack.append(array[i])
        else:
            while stack and array[i] > stack[-1]:
                top = stack.pop()
                op[array.index(top)] = array[i]
            stack.append(array[i])
    while stack:
        top = stack.pop()
        op[array.index(top)] = -1
    print(op)


a = [9, 7, 2, 4, 6, 8, 12, 1, 5]
optimised_next_greater_element(a)
