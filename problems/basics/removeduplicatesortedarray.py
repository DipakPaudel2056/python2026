# we are using two pointers
# and returning index with non repeated sorted elements
def remove_duplicate(arr):
    i = j = 0
    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        j += 1
        
    return i
            
print(remove_duplicate([1,2,2,2,2,3,3,3,3,4]))