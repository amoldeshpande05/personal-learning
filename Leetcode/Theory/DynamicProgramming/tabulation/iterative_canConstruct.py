def canConstruct(target,words):
    dp=[False]*(len(target)+1)
    
    dp[0] = True
    
    for dpIndex in range(0,len(dp)):
        if dp[dpIndex] == True:
            for word in words:
                if target[dpIndex:].find(word) == 0:
                    dp[dpIndex+len(word)] = True
                    
    return dp[len(target)]



print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("purple",["purp","p","ur","le","purpl"]))