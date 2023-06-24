# 2090. K Radius Subarray Averages
# You are given a 0-indexed array nums of n integers, and an integer k.

# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

# For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

# Example 1:

# Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]
# Explanation:
# - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
# - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
#   Using integer division, avg[3] = 37 / 7 = 5.
# - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
# - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
# - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.

# Example 2:

# Input: nums = [100000], k = 0
# Output: [100000]
# Explanation:
# - The sum of the subarray centered at index 0 with radius 0 is: 100000.
#   avg[0] = 100000 / 1 = 100000.

# Example 3:

# Input: nums = [8], k = 100000
# Output: [-1]
# Explanation:
# - avg[0] is -1 because there are less than k elements before and after index 0.

# Solution : Time Limit Exceeded
def getAverages(nums, k):
    n = len(nums)
    res = []
    for i in range(n):
        if i - k < 0 or i + k >= n:
            res.append(-1)
            continue
        res.append(sum(nums[i-k:i+k+1])//(2*k+1))
    return res

# Constraints:
# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i], k <= 105


def getAverages2(nums, k):
    n = len(nums)
    res = []
    if k == 0:
        return nums
    if k > n:
        return [-1]
    for i in range(n):
        if i - k < 0 or i + k >= n:
            res.append(-1)
            continue
        res.append(sum(nums[i-k:i+k+1])//(2*k+1))
    return res


print(getAverages2([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
print(getAverages2([100000], 0))
print(getAverages2([8], 100000))

# Runtime: 1124 ms, faster than 100.00% of Python3 online submissions for K-Radius Subarray Averages.
# Memory Usage: 30.1 MB, less than 100.00% of Python3 online submissions for K-Radius Subarray Averages.
# Time Limit Exceeded
# Need to optimize
# Solution : Accepted

def getAverages3(nums, k):
    prefsum=[0]
    for i in range(len(nums)):
        prefsum.append(prefsum[-1]+nums[i])
    i,j=0,len(nums)-1
    # return prefsum
    output=[]
    for x in range(len(nums)):
        if x-k<i or x+k>j:
           output.append(-1)
        else:
            if x-k>0:
                avg=prefsum[x+k+1]-prefsum[x-k]
            else:
                avg=prefsum[x+k+1]
            avg//=(2*k+1)
            output.append(avg)
    return output

print(getAverages3([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
print(getAverages3([100000], 0))
print(getAverages3([8], 100000))