# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1




class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if i in temp.keys():
                temp[i]+=1
            else:
                temp[i]=1
        max_value = max(temp, key=temp.get)
        return max_value


# this is the 2nlogn time complexity and O(n) space complexity


# Now after reading a program we understood that, if we get just 1 element which is greater than n/2, then just stop and print it, by this, just return the element which is greater than n/2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if i in temp.keys():
                temp[i]+=1
                if temp[i] >= (len(nums)/2):
                    return i
            else:
                temp[i]=1
        return nums[0]
    
    
#  We have to come with with a solution so that the space complexity is O(1) and time complexity should be O(n)
# How to do that?
# To solve this problem, we have to go through moore's voting algorithm
# Logic is as follows, you take a number, if you find the similar number in the next iteration, increase the count, or decrease the count, if count = 0, then move to next element, by doing this, you will end up with the number which will be equal to the element which is in majority

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ansIndex = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == nums[ansIndex]:
                count+=1
            else:
                count-=1
            if count == 0:
                ansIndex = i
                count = 1
        
        return nums[ansIndex]