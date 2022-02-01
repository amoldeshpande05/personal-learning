# Kadane's Algorithm
# This approach is based on Kandane's algorithm, which states that, there can never be -ve maxSum subarrays with more than 1 value. when you hit negative, stop right there, each iteration calculate the maxSum.
# maintain 2 variables, 1 for maxprofit and 2 for currSum



def maxProfit(nums):
    currSum=0 #to hold the sum of the current subarray
    maxSum=nums[0] #To hold the sum of the maxSum of various sub arrays
    
    
    for i in nums:
        currSum+=i
        # Add the profit
        if maxSum < currSum:
            maxSum = currSum
        
        if currSum<0:
            currSum=0
    return maxSum