
#   The best solution is surprisingly confusing, just take the a new blank matrix, based on the new rows and columns. construct the mattrix accodingly and return the result
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        newMatrix=[[]]
        newR = 0
        newC = 0
        
        for i in range(0,m):
            for j in range(0, n):
                if newC < c:
                    newC+=1
                else:
                    newMatrix.append([])
                    newC=1
                    newR+=1
                newMatrix[newR].append(mat[i][j])
                
        return newMatrix
                
        
         
                
             
            