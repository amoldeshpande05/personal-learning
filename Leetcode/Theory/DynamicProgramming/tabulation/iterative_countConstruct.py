def countConstruct(target,words):
    dp=[0]*(len(target)+1)
    dp[0]=1

    for index in range(len(dp)):
        if dp[index]>0:
            for word in words:
                if target[index:].find(word) == 0:
                    dp[index+len(word)]+=dp[index]
            
    return dp[len(target)]

print(countConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(countConstruct("purple",["purp","p","ur","le","purpl"]))