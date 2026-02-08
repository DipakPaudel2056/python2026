# Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.

# Examples:

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: The sorted array will be [1, 3, 4, 7, 9].

class Solution:
    def insertionSort(self, arr):
        # code here
        # the idea behind the insertion sort is divide the arr into two part
        n = len(arr)
        for i in range(1,n):
            insert_index = i
            current_value = arr.pop(i)
            
            for j in range(i-1,-1,-1):
                if arr[j] > current_value:
                    insert_index = j
            arr.insert(insert_index,current_value)
        return arr


