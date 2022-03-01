from turtle import clear


def bestSum(targetSum,numbers):
    dp = [None]*(targetSum+1)
    dp[0] = []
    for dpIndex in range(0,len(dp)):
        for i in numbers:
            if dp[dpIndex]!= None and dpIndex+i <= targetSum:
                temp =  dp[dpIndex] + [i]
                if dp[dpIndex+i] == None or len(temp) < len(dp[dpIndex+i]):
                    dp[dpIndex+i] = temp

    return dp[targetSum]
print("The sum is:",bestSum(100,[1,2,5,25]))