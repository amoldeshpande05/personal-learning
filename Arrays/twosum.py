# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#  The logic goes as follows, the hint is that there will two numbers which adds up to the target, since we know the target, how to get the two numbers?????? 1st check the condition!!!!! if target - ith number, whatever the difference we get, is the difference there in the list??? if yes, then return the two values, the difference present and the ith number. if not then append the ith number into the hasmap or a dictionary!




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] =  i  
        return