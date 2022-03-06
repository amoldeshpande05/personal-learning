# Here in our program, let's use recurssive method to find all the combination of opening and closeing parenthsis. Store the opening and closing parenthisis combination in the stack, where we append when we are trying to find the ith combination, when that is exhausted, pop it find ith-1 combination
# First is the stopping condition which is openN == closeN == n, when this thing happens, join the stack in order to make a complete string and append it to the result.
# To add a opening paranthesis, the condition is that openN<n
# for closing the condition is closeN<openN
# return result
# For more explaination https://www.youtube.com/watch?v=s9fokUqJ76A&t=614s



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        
        def helper(openN,closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                helper(openN+1,closeN)
                stack.pop()
            
            if closeN<openN:
                stack.append(")")
                helper(openN,closeN+1)
                stack.pop()
        
        helper(0,0)
        return res
            
                
        
        



        
