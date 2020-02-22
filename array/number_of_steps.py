def number_of_ways(n):
    """
    Function to get the number of ways one can reach n steps if only 1/2/3 steps are allowed at a time.
    This works like fibonaci series where we store answers of initial values and use them to calculate answers of above
    values.
    The number of ways to reach n steps is equal to sum of ways to reach (n-1), (n-2), and (n-3) steps
    :param n: Int
    :return: Int
    """
    initial_ways = {
        1: 1,
        2: 2,
        3: 4
        }
    if n in initial_ways:
        return initial_ways[n]
    else:
        ways = number_of_ways(n-1) + number_of_ways(n-2) + number_of_ways(n-3)
        if n not in initial_ways:
            initial_ways[n] = ways
        return ways
    

x = number_of_ways(5)
print(x)
