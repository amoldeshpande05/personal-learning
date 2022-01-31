# This approach is bottom up approach and works fine!!

class Solution:
    def tribonacci(self, n: int) -> int:
        result = [0]*(n+1)
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            result[0] = 0
            result[1] = 1
            result[2] = 1
        
        for i in range(3,n+1):
            result[i]=result[i-1] + result[i-2] + result[i-3]
            
        return result[n]
    
    
    
# This approach is top down approach

class Solution:
    def tribonacci(self, n: int,memo={}) -> int:
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return memo[n]
    
    
    
    
    # No need of explaination... It's a basic addition to the fibonacci.