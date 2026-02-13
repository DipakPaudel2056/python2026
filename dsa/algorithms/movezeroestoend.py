# here array is given, we need to move them to the end
# so we use threee pointer method here

def move_zeroes(arr):
    left= 0 
    right = len(arr)-1
    
    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left],arr[right]=arr[right],arr[left]
            left += 1
            right -= 1
        if arr[right] == 0:
            right -= 1
        left += 1
    return arr

print(move_zeroes([0,0,0,0,0,0,0,1]))