def total_rain_water(a):
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
    print(left_max, right_max)
    total = 0
    for i in range(len(a)):
        lower = min(left_max[i], right_max[i])
        if lower - a[i] > 0:
            total += (lower - a[i])
    return total


a = [2, 0, 2]
x = total_rain_water(a)
print(x)
