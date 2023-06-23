def reverseArray(a, low=0, high=None):
    if high == None:
        high = len(a) - 1
    if low >= high:
        return a
    a[low], a[high] = a[high], a[low]
    return reverseArray(a, low + 1, high - 1)
# one line solution in python
# def reverseArray(a):
#     return a[::-1]


print(reverseArray([1, 2, 3, 4, 5]))
