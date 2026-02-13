# for this approach we can eith user frequency, table, hashmap, or XOR operator
def findUnique(arr):
    a= 0
    for i in range(len(arr)):
        a ^= arr[i]
    return a

print(findUnique([1,2,3,4,5,6,2,3,4,5,1]))