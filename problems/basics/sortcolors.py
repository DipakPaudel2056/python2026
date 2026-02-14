
arr = [0,1,0,2,2,1]
# now sort them using three pointers method

def three_pointer_sort(arr):
    current_index = 0
    zero_index = 0
    two_index = len(arr)-1
    while current_index <= two_index:
        if arr[current_index] == 0:
            [arr[current_index],arr[zero_index]] = [arr[zero_index],arr[current_index]]
            zero_index += 1
            current_index += 1
        if arr[current_index] == 1:
            current_index += 1
        if arr[current_index] == 2:
            [arr[current_index],arr[two_index]] = [arr[two_index],arr[current_index]]
            two_index -= 1


three_pointer_sort(arr)
print(arr)

# leetcode question 75