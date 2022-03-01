# Solutrion is straight fowrd, take a variable and go on adding the values frm begining and send the new count
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        validSize=0
        for index,value in enumerate(nums):
            if value !=val:
                nums[validSize]=value
                validSize+=1
        return validSize