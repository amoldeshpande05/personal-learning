# https://leetcode.com/problems/coin-change/submissions/
# The solution is the basic dynamic programming concept, where we an choose a tabulation method to add all the values in the list with -1 initially. write down the basic test condition where for no elements the result will be zero. Based on that just go on counting on how many coins we can reach the i'th amount and add a logic for optimisim and bingo, you reach the result
# n = amount m=len(coins)
# TimeComplexity : O(m*n)
# spaceComplexity: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        dp[0]=0
        for dpIndex in range(len(dp)):
            for coin in coins:
                if dp[dpIndex] != -1 and dpIndex+coin <=amount:   
                    if dp[dpIndex+coin]==-1 or dp[dpIndex+coin] > dp[dpIndex]+1:
                        dp[dpIndex+coin] = dp[dpIndex]+1
        return dp[amount]
                        
                        