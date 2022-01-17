def binarySearch(nums,element):
   
   l=0
   r=len(nums) - 1
   m=0
   while l <= r:
       m = int((l + r) / 2)
       if nums[m] == element:
           return m
       if element < nums[m]:
           r = m - 1
       else:
           l = m + 1
   return r
        


print(binarySearch([1,3,5,6],5))
    