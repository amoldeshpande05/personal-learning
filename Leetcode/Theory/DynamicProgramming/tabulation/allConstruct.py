def allConstruct(target,words):
    # dp=[]*(len(target)+1)
    dp=[]
    for i in range(len(target)+1):
        dp.append([])
        
    dp[0]=[[]]

    for index in range(len(dp)):
        if dp[index] != []:
            temp=[]
            for word in words:
                if target[index:].find(word) == 0:
                    for i in range(len(dp[index])):
                        dp[index+len(word)].append(dp[index][i] + [word])

            
    return dp[len(target)]

print(allConstruct("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
# print(allConstruct("purple",["purp","p","ur","le","purpl"]))

# Time complexity = for every target
# m = len(target)
# n = len(words)
# O(m*n)