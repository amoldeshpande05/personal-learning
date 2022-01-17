# 35. Search Insert Position
# Easy

# 6309

# 363

# Add to List

# Share
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
# Accepted
# 1,186,246


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums) - 1
        m=0
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l

# The logic goes as follows, write a binary search and when the element it not found, if we trace the code, left(l) will always have the index where the element should have been