# 1732 Find the Highest Altitude
# There is a biker going on a road trip. The road trip consists of n + 1 
# points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain
# in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example 2:
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

# Solution: Accepted
# Runtime: 24 ms
# Memory Usage: 13.4 MB
# Time Complexity: O(n)
def largestAltitude(gain):
    max_alt = 0
    alt = 0
    for i in gain:
        alt += i
        if alt > max_alt:
            max_alt = alt
    return max_alt

print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))