# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [2, 1, 4, 3, 5]
# Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

# Input: arr[] = [2, 4, 7, 8, 9, 10]
# Output: [4, 2, 8, 7, 10, 9]
# Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.

# Try it on GfG Practice
# redirect icon
# [Approach] Adjacent Pair Swapping Method
# The main idea of this approach is to rearrange it into a wave form by swapping adjacent elements in pairs.

# Since, the elements are in increasing order. Then, by swapping every pair of adjacent elements (i.e., arr[0] with arr[1], arr[2] with arr[3], and so on), we create a pattern where:

# Every even index i holds a value greater than or equal to its neighboring odd indices i - 1 and i + 1 (if they exist).
# This guarantees the wave condition: arr[0] ≥ arr[1] ≤ arr[2] ≥ arr[3] ≤ arr[4] ≥ ...
# The sorted array ensures the numbers are close enough to form valid wave peaks and valleys, and the pairwise swaps are what enforce the pattern.


def sort_arr(arr):
    n = len(arr)
    # so we just have to check the odd index and see if it is greater than the previous and next item
    for i in range(1,n,2):
        print(i,arr[i])
        if arr[i] < arr[i-1]:
            print(i,'back-swap')
            arr[i],arr[i-1]=arr[i-1],arr[i]
            print(arr)
            print("====")
        if i+1 < n and arr[i] < arr[i+1]:
            print(i,"front-swap")
            arr[i],arr[i+1] = arr[i+1],arr[i]
            print(arr)
            print("====")
    return arr

print(sort_arr([2,5,6,7,4,1]))