def rotateArray(a, d):
    n = len(a)
    d = d % n
    a = a[d:] + a[:d]
    return a


print(rotateArray([1, 2, 3, 4, 5], 2))
# [3, 4, 5, 1, 2]
