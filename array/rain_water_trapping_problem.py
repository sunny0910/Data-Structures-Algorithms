def total_rain_water(a):
    """
    Rain water trapping problem
    Function to calculate the amount of rain water trapped between the elements.
    Time complexity O(n) and space complexity O(n) as it uses two auxiliary arrays to pre-compute left and right max
    :param a: List
    :return: Int
    """
    left_max = [0]*len(a)
    right_max = [0]*len(a)
    high = 0
    for i in range(len(a)):
        if a[i] > high:
            high = a[i]
        left_max[i] = high
    high = 0
    for i in range(len(a)-1, -1, -1):
        if a[i] > high:
            high = a[i]
        right_max[i] = high
    total = 0
    for i in range(len(a)):
        lower = min(left_max[i], right_max[i])
        if lower - a[i] > 0:
            total += (lower - a[i])
    return total


def optimised_total_rain_water(a):
    """
    Optimised rain water trapping approach as it just uses 2 variable space for left max and right max instead of two
    arrays in the above approach.
    This calculates water for lower elements first with low = 0 and high = n-1 until they cross each other.
    :param a: List
    :return: Int # Amount of water
    """
    low = 0
    high = len(a)-1
    result = 0
    left_max = 0
    right_max = 0
    while low < high:
        if a[low] < a[high]:
            if a[low] > left_max:
                left_max = a[low]
            else:
                result += left_max - a[low]
            low += 1
        else:
            if a[high] > right_max:
                right_max = a[high]
            else:
                result += right_max - a[high]
            high -= 1
    return result


a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
x = optimised_total_rain_water(a)
print(x)
