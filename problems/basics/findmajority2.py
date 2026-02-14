# here you need to find 2 elements in the array that are more than N/3 times
def find_majority(nums):
    candidate1 = 0
    candidate2 = 0
    vote1 = 0
    vote2 = 0
    for ele in nums:
        if candidate1 == ele:
            vote1 += 1
        elif candidate2 == ele:
            vote2 += 1
        elif vote1 == 0:
            candidate1 = ele
            vote1 += 1
        elif vote2 == 0:
            candidate2 = ele
            vote2 += 1
        else:
            vote1 -= 1
            vote2 -= 1
            
    res = []
    cnt1,cnt2=0,0
    
    for ele in nums:
        if candidate1 == ele:
            cnt1 += 1
        if candidate2 == ele:
            cnt2 += 1
    
    if cnt1 > len(nums) / 3:
        res.append(candidate1)
    if cnt2 > len(nums)/3:
        res.append(candidate2)
        
    if len(res) == 2 and res[0] > res[1]:
        res[0],res[1] = res[1],res[0]
        
    return res        

print(find_majority([1,2,3,3,3,2,3,2,5,2,6,2,3,3]))