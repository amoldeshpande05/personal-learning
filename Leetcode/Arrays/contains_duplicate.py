class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
        # hold={}
        # for i in nums:
        #     if i not in hold:
        #         hold[i]=1
        #     else:
        #         return True
        # return False
        
# Input: nums = [1,2,3,1]
# Output: true
# Input: nums = [1,2,3,4]
# Output: false
# If anything is repeated twice, then return true or return False



# The logic is that, store a dictionary and keep on adding the element, if you find any duplicate then return false or return true