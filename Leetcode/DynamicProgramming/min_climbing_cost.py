# The solution goes as follows, what is dynamic programming??? we have to consider two things, what is the stopping condition and what is the solution for ith step, in the min climbing cost problem, there are two possiblities, 1 is you can start from 1st step or you can start from 2nd step, which in terms of top down approach either n or n-1, so the function will take 1 starting point and calculate all the possible combination with the formula cost[i] + min(helper(n-1),helper(n-2))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n,memo={}):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0
            if n == 1 or n == 0:
                return cost[n]
            
            memo[n] = cost[n]+ min(helper(n-1),helper(n-2)) 
            return memo[n]
        
        return min(helper(len(cost)-1),helper(len(cost)-2))