def howSum(targetSum,numbers):
    dp = [None]*(targetSum+1)
    dp[0] = []
    for dpIndex in range(0,len(dp)):
        for i in numbers:
            if dp[dpIndex]!= None and dpIndex+i <= targetSum:
                dp[dpIndex+i] = dp[dpIndex] + [i]
                # dp[dpIndex+i].append(i)
                print(dp[dpIndex+i])
                # dp[dpIndex+i].append(i)
                # print(dp,dpIndex+i)

                # print(dp[dpIndex+i])
                # 
        
    return dp[targetSum]
   
# [[4], None, None, None, [4], None, None, None] 4
# [[4, 3], None, None, [4, 3], [4, 3], None, None, None] 3
# [[4, 3, 4], None, None, [4, 3, 4], [4, 3, 4], None, None, [4, 3, 4]] 7
# [[4, 3, 4, 3], None, None, [4, 3, 4, 3], [4, 3, 4, 3], None, [4, 3, 4, 3], [4, 3, 4, 3]] 6
# [[4, 3, 4, 3, 3], None, None, [4, 3, 4, 3, 3], [4, 3, 4, 3, 3], None, [4, 3, 4, 3, 3], [4, 3, 4, 3, 3]] 7
# The sum is: [4, 3, 4, 3, 3]



print("The sum is:",howSum(7,[4,3]))