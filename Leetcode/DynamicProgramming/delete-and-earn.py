
# The solution is amazing, by this I realized that for dynamic programming, please go for bottom up approach instead of complicated top down approach which is easy to visualize. 
# The solution goes as follows, let's go back to house robber problem, where we had decision to make either to pick1 or pick2, the problem is similar after tweeking a little, how to do that? make the counter, sort the array because of this hint
# If you take a number, you might as well take them all. Keep track of what the value is of the subset of the input with maximum M when you either take or don't take M
# Based on the above hint, go on calculating for just 1 number what? For 2 numbers how to calculate, for 3 numbers we check if previous is == nums[i]-1, if it is, the take the max either curr+pp or p, based on that move forward, 



class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums=sorted(list(set(nums)))
        p,pp = 0,0
        for i in range(len(nums)):
            currSum=count[nums[i]]*nums[i]
            
            if i > 0 and nums[i]-1 == nums[i-1]:
                currSum= max(p,pp+currSum)
            else:
                currSum+=p
            pp=p
            p=currSum
        return p
            
            
        
        
        
        