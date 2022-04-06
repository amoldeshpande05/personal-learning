# The logic is that all the 0's should be in the begining and 2's should be at the end, which leaves 1 in the middle, so what we will do is that to take two pointers, l and r. let i be independent iteration variable based on which we will swap l and r, whenever i encounters 0, we will swap with l, whenever i encounters 2 we will swap with r, but we should make sure that when we swap 2 with r, they may be chance that r is pointing towards 2 or 0, we dont want 2 or zero in the middle, so we will make sure we dont increment i when 2 is encountered


class Solution:
    def sortColors(self, nums: List[int]) -> None:
       i=0
       l=0
       r=len(nums)-1

       while i<=r:
           if nums[i] == 0:
               nums[l],nums[i]=nums[i],nums[l]
               l+=1
           elif nums[i] == 2:
               nums[r],nums[i]=nums[i],nums[r]
               i-=1
               r-=1
           i+=1


                