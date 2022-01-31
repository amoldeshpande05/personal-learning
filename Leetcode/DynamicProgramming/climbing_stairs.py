# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def __init__(self):
        self.memo={}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
          
        if (n-1,n-2) in self.memo.keys():
            return self.memo[(n-1,n-2)] 
        else:
            self.memo[(n-1,n-2)] = self.climbStairs(n-1) + self.climbStairs(n - 2)
            return self.memo[(n-1,n-2)]

# Simple straight forword dynamic programming concept