# Given n ranges, find the maximum appearing element in the ranges.
# Sample Input: L[] = {1, 2, 5, 15}, R[] = {5, 8, 7, 18}
# Sample Output: 5
# Explanation:
# [1, 5] appears 1,2,3,4,5
# [2, 8] appears 2,3,4,5,6,7,8
# [5, 7] appears 5,6,7
# [15, 18] appears 15,16,17,18
# Hence, 5 appears maximum number of 3 times.

def max_appearing_element(l, r):
    arr = [0] * 1000
    for i in range(len(l)):
        arr[l[i]] += 1
        arr[r[i] + 1] -= 1
    max_element = arr[0]
    result = 0
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
        if max_element < arr[i]:
            max_element = arr[i]
            result = i
    return result


print(max_appearing_element([1, 2, 5, 15], [5, 8, 7, 18]))
