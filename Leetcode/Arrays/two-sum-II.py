# Description
# The logic goes as follows, This is a two pointer approach to find out the two numbers, we will have  pointer A at the begining and pointer B at the end, first we check if those 2 add up, if it doesnt, we will see if the sum is greater or lesser, if it's greater then decrement the pointer B or increment the pointer A untill you find the solution

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointA=0
        pointB=len(numbers)-1
        
        while pointA<pointB:
            currSum = numbers[pointA] + numbers[pointB]
            if currSum > target:
                pointB-=1
            elif currSum < target:
                pointA+=1   
            else:
                return [pointA+1,pointB+1]
                
