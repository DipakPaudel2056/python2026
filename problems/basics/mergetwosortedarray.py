def mergetwosorted(arr1,arr2):
    # for this problem we want to use two pointers method
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    resultArr = []
    
    while(i < n and j < m):
        if arr1[i] < arr2[j]:
            resultArr.append(arr1[i])
            i += 1
        else:
            resultArr.append(arr2[j])
            j+=1
    while i < n:
        resultArr.append(arr1[i])
        i+=1
    while j < m:
        resultArr.append(arr2[j])
        j+=1
    return resultArr
            
    
print(mergetwosorted([4,7,8,10],[2,5,6,9]))
            