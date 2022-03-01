nums = [0,1,2,3,4,5]


def helper(l,r):
    if l>r:
        return None
    
    m = (l+r) // 2
    print(nums[m])
    helper(l,m-1)
    helper(m+1,r)

helper(0,len(nums)-1)
