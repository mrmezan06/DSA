# Given an array of integers of size ‘n’. Calculate the maximum sum possible for ‘k’ consecutive elements in the array.
# Sample Input: 1,2,3,1,4,5
#               k = 3
# Sample Output: 10

def MaxSum(arr, k):
    if len(arr) < k:
        print("Invalid Operation")
        return -1
    maxSum = 0
    for i in range(k):
        maxSum += arr[i]
    windowSum = maxSum
    # range(start, stop)
    for i in range(k, len(arr)):
        windowSum += arr[i] - arr[i-k]
        maxSum = max(maxSum, windowSum)
        # print(arr[i])
    return maxSum


print(MaxSum([1, 2, 3, 1, 4, 5], 3))
