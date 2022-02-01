# https://leetcode.com/problems/sum-of-unique-elements/submissions/


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        temp={}
        result=0
        for index,value in enumerate(nums):
            if value not in temp:
                temp[value]=value
                result+=value
            else:
                if result>0 and temp[value]:
                    result-=value
                temp[value]=False        
        return result
        
    # Most efficient way
    
    
    
    
    