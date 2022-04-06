

# champagne-towers
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        result = [[0]*k for k in range(1,102)]
        result[0][0]=poured
        
        for i in range(0,100):
            for j in range(0,i+1):
                if result[i][j] > 1:
                    result[i+1][j] += (result[i][j]-1)/2
                    result[i+1][j+1] += (result[i][j]-1)/2
                    result[i][j]=1
        return result[query_row][query_glass]



        
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        result = [[0]*k for k in range(1,102)]        
        result[0][0]=poured
        for i in range(0,100):
            for j in range(0,i+1):
                if result[i][j] > 1:
                    result[i+1][j] += (result[i][j]-1)/2
                    result[i+1][j+1] += (result[i][j]-1)/2
                    result[i][j]=1
        return result[query_row][query_glass]
        
