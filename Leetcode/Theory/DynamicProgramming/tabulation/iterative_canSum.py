def canSum(targetSum,numbers):
    
    # 7,[2,3]
    dp = [False]*(targetSum+1)
    dp[0] = True
    for dpIndex in range(0,len(dp)):
        if dp[dpIndex] == True:
            for i in numbers:
                if dpIndex+i <= (len(dp)-1):
                    dp[dpIndex+i] = True
    print('The dp array is  : ',dp)
    return dp[targetSum]



print("The sum is:",canSum(7,[3,4]))