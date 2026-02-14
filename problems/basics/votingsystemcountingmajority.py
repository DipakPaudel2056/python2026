# you are given an array, now you need to find what is the majority of element i.e. N/2 time occuring element
# we can use hashmap to store the frequency and check if any values are greater than N/2 but in terms of memory if every element are occuring only once, then it will be 2N
# so the approach we are taking today is voting system approach,

def find_majority(arr):
    majority = 0
    result = 0
    for n in arr:
        if majority == 0:
            result = n
        if n == result:
            majority += 1
        else:
            majority -= 1
    return result
    
print(find_majority([1,1,0,1,5,1,6,7,1,1,8]))

# leetcode 169