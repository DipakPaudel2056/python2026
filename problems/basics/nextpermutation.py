def next_per(nums):
    pivot_index = -1
    j = len(nums) - 1
    n = len(nums) - 1
    for j in range(n,0,-1):
        if nums[j-1] > nums[j]:
            pivot_index = j-1
            break
        
    if pivot_index == -1:
        nums.reverse()
        return
    
    for i in range(n-1,pivot_index,-1):
        if nums[i] > nums[pivot_index]:
            nums[pivot_index],nums[i]=nums[i],nums[pivot_index]
            break
    
    left,right=pivot_index+1,n-1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
    return nums
        
print(next_per([2,4,1,7,5,0]))