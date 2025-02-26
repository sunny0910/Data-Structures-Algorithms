def min_platforms(arr, dep):
    """
    Railway platform problem.
    Function to get the minimum number of platforms required for trains using their arrival and departure timings.
    :param arr: List
    :param dep: List
    :return: Int
    """
    if not arr or not dep:
        return
    arr.sort()
    dep.sort()
    i = 1
    j = 0
    platforms = 1
    max_platforms = platforms
    while i < len(arr) and j < len(dep):
        if arr[i] < dep[j]:
            platforms += 1
            i += 1
            if platforms > max_platforms:
                max_platforms = platforms
        else:
            platforms -= 1
            j += 1
    return max_platforms


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
x = min_platforms(arr, dep)
print(x)
