# Two point approach, where i will begin from zero, j exceeds, when the proper condition meets, swap it accordingly

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=1
        while i < len(nums) and j < len(nums) :
            if nums[i] == 0 and nums[j] == 0:
                j+=1
                continue
            if nums[i] == 0 and nums[j] !=0:
                temp = nums[i]
                nums[i]=nums[j]
                nums[j]=temp
            j+=1
            i+=1
        
            
                
                
                
      
                    