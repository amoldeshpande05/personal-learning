# Initial attempt with [[]] list of list's combination
# problem is that 1 1 2 and 1 2 1 both consider different number of coins which is wrong with respect to the leetcode problemt
# I have resolved it by sorting it and then storing it, while storing it, compare if the sorted combination is already there, this works fine but takes too long to compute

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp=[[]]*(len(amount)+1)
        dp=[]
        for i in range(amount+1):
            dp.append([])
        dp[0]=[[]]
        
        
        for dpIndex in range(len(dp)):
            if len(dp[dpIndex])>0:
                for coin in coins:
                    if dpIndex+coin <= amount:
                        
                        for i in dp[dpIndex]:
                            temp=i+[coin]
                            temp.sort()
                            if temp not in dp[dpIndex+coin]:
                                dp[dpIndex+coin].append(temp)
    
        
        
        return len(dp[amount])
    
    
    
# Prefered solution
# The logic goes like this, since we have to find out the unique combination which are possibe to get the final coin, so normal dp approach is not valid, it returns us all the possible combination like 1 2 2 and 2 2 1 which is not valid in our case
# To resolve this problem, we consider a matrix where rows represent the elements and columns represent the sum at jth position
# if the sum is not possible then simply add the above value or zero if it's first row.
# i
    
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp=[[]]*(len(amount)+1)
        dp=[]
        for i in range(len(coins)):
            temp = [0]*(amount+1)
            temp[0]=1
            dp.append(temp)
            
        for i in range(0,len(dp)):
            for j in range(1,len(dp[0])):
                wcc = 0
                if i > 0:
                    wcc=dp[i-1][j]
                    
                if j < coins[i]:
                    dp[i][j]=wcc
                else:
                    dp[i][j]=wcc+dp[i][j-coins[i]]
                        
        
        return dp[-1][-1]