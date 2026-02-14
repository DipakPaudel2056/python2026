# 643. Maximum Average Subarray I
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 
def findmaxaveragesubarray(nums,k):
    k_sum = sum(nums[:k])
    m = k_sum
    for i in range(k,len(nums)):
        k_sum += nums[i]
        k_sum -= nums[i - k]
        m = max(m,k_sum)
        
    return m/k # return average

print(findmaxaveragesubarray([1,12,-5,-6,50,3],4))