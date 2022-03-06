# Read the question properly, they said it's a continuous solution(airthmetic slices) 
# When we go on solving it for 1 2 3 4 5 6 7, we tend to see a pattern, for 1 2 3, the soln is 1(way)-> which is increment by 1 from 0, for 1 2 3 4, the solution is 3 -> which is previous result + increment of curr by 1, which is 2, so the result will be curr++ and result += curr that is 1+2 =>3 and so on ...

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        curr = 0
        total=0
        for i in range(2,len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr+=1
                total+=curr
            else:
                curr=0
        return total