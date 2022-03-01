# Soln is straight forward. inirialize an array for output if numRows=1, Start the loop from 1,n. define a function to return a list for pascal's list at nth position

class Solution:
    def pascalSum(self,arr):
        result=[]   
        temp = 0
        for i in arr:
            temp+=i
            result.append(temp)
            temp=i
        result.append(1)
        return result
        
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0:
            return []
        result=[[1]]
        if numRows == 1:
            return result
        
        for i in range(1,numRows):
            result.append(self.pascalSum(result[i-1]))
        return result
            
            