# 1027. Longest Arithmetic Subsequence
# Explanation:
# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
# Note that:
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

# Example 1:
# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

# Example 2:
# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:  The longest arithmetic subsequence is [4,7,10].

# Example 3:
# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].
# Solution: Accepted

def longestArithSeqLength(nums):
    n = len(nums)
    if n < 3:
        return n
    dp = [{} for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            dp[i][d] = dp[j].get(d, 1) + 1
            res = max(res, dp[i][d])
    return res


print(longestArithSeqLength([3, 6, 9, 12]))
print(longestArithSeqLength([9, 4, 7, 2, 10]))
print(longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
