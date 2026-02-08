# # You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

# Examples:

# Input: arr[] = [1, 2, 3, 5]
# Output: 4
# Explanation: All the numbers from 1 to 5 are present except 4.
# Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
# Output: 6
# Explanation: All the numbers from 1 to 8 are present except 6.


# for this we have a trick also called as gauss algorithm
# get the total sum from the given array
# calculate the expected sum for the arithmetic series upto that length
# decrease the total sum from the expected sum

class Solution:
    def missingNum(self, arr):
        # code here
        arrsum = 0
        expectedsum =0
        n = len(arr)
        k=n+1
        for i in range(len(arr)):
            arrsum = arrsum + arr[i]
        expectedsum = k*(k+1)/2
        return int(expectedsum-arrsum)
            