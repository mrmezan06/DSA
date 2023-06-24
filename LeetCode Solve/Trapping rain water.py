# Trapping rain water
# Sample input: 2, 0, 2
# Sample output: 2
# Sample input: 3, 0, 1, 2, 5
# Sample output: 6

def trap_rain_water(a):
    n = len(a)
    left = [0] * n
    right = [0] * n
    left[0] = a[0]
    right[n - 1] = a[n - 1]
    for i in range(1, n):
        left[i] = max(left[i - 1], a[i])
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], a[i])
    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - a[i]
    return water

# Time Complexity: O(n)


print(trap_rain_water([3, 0, 1, 2, 5]))
print(trap_rain_water([2, 0, 2]))
