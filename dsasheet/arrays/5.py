def negative_left(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i]>0:
            while j >=0 and nums[j] > 0:
                j-=1
            if j<i:
                return nums
            nums[i],nums[j]=nums[j],nums[i]
        i+=1
    return nums

print(negative_left([-1,2,-3]))