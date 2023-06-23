# Given a fixed array and multiple queries of following types on the array, how to efficiently perform these queries.
# Sample Input: 2, 8, 3, 9, 6, 5, 4
# Queries:
# 1. Sum of subarray from index 0 to 2
# 2. Sum of subarray from index 1 to 3
# 3. Sum of subarray from index 2 to 6
# Sample Output: 13, 20, 27

def prefix_sum(arr, start, end):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    # print(prefix_sum)
    return prefix_sum[end] - prefix_sum[start-1] if start > 0 else prefix_sum[end]


arr = [2, 8, 3, 9, 6, 5, 4]
print(prefix_sum(arr, 0, 2), end=" ")
print(prefix_sum(arr, 1, 3), end=" ")
print(prefix_sum(arr, 2, 6))
