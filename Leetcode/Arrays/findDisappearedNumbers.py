# 448. Find All Numbers Disappeared in an Array
# Easy

# 5839

# 354

# Add to List

# Share
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.




# Faltu Logic


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums=set(nums)
        ansList=[]
        for i in range(1,length + 1):
            if i not in nums:
                ansList.append(i)
        return ansList
                
                
# convert into set and check with O(n^2)

# Best logic


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1]*=-1
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
                