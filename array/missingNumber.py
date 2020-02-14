def missing_number(a, start, end):
    mid = (start+end) // 2
    if (a[mid] - mid) == 2 and (a[mid-1] - (mid-1)) == 1:
        return a[mid]-1
    elif a[mid] - mid == 1:
        return missing_number(a, mid+1, end)
    return missing_number(a, start, mid-1)


a = [1, 2, 3, 4, 6, 7, 8]
x = missing_number(a, 0, len(a))
print(x)
