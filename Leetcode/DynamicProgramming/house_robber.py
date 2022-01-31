# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400




class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurCall(i,memo={}):
            if i in memo:
                return memo[i]
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i],nums[i-1])
            
            memo[i] = max(recurCall(i-1),recurCall(i-2)+nums[i])
            return memo[i]
        
        return recurCall(len(nums)-1)
                
            
        
# The approach goes like this, before starting any dp program, right down the base cases, if i = 0 then we have only one house assuming that index starts from 0, so we will return the same value, if i == 1, which means we have two houses, in this case, we have to find the maximum of these two houses, which is max(nums[i], nums[i-1]), so there goes our base case
# now comes the part of general solution, assuming that the two base cases are taken care, let's assume our i = n, then at the top what we want is the max(recurCall(i-1),recurCall(i-2)+nums[i]) by this the right value is returned.
# The above approach is top down aproach, now let's see, how can we go for tabulation approach which is bottom up approach


# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         results=[0]*len(nums)
#         if len(nums) == 1: 
#             return nums[0]
#         results[0]=nums[0]
#         results[1] = max(nums[0],nums[1])
#         for i in range(2, len(nums)):
#             results[i] = max(results[i-1],results[i-2]+nums[i])
#         return results[-1]
        
        
# The above approach will make sure it has all the values in the list