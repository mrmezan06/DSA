# Given an array of integers, find if it has an equilibrium point.
# Sample Input: 3, 4, 8, -9, 20, 6
# Sample Output: True
# Explanation: 20 is the equilibrium point as 3 + 4 + 8 - 9 = 20 + 6
# Sample Input: 4, 2, -2
# Sample Output: True
# Explanation: 4 is the equilibrium point as 2 + (-2) = 0 and left side sum is also 0 because there is no element on the left side
# Sample Input: 4, 2, 2
# Sample Output: False
# Explanation: No equilibrium point

def equilibrium_point(arr):
    left_sum = 0
    right_sum = sum(arr)
    for i in range(len(arr)):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return True
        left_sum += arr[i]
    return False


print(equilibrium_point([3, 4, 8, -9, 20, 6]), end=" ")
print(equilibrium_point([4, 2, -2]), end=" ")
print(equilibrium_point([4, 2, 2]))
