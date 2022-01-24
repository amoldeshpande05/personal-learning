# 'abcdef' with word bank ['ab','abc','cd','def','abcd','ef','c'] then answer should be 
# [
#   [ 'ab', 'cd', 'ef' ],
#   [ 'ab', 'c', 'def' ],
#   [ 'abc', 'def' ],
#   [ 'abcd', 'ef' ]
# ]


# This technique is amazing, when the question like this arrives, to proceed, take the board, draw the chart and come from bottom of the chart. Main intention should be what each of the recurssion should return
# We start with the base case, if nothing is present then please have [[]] as a value, then go on the recurssion, keep on adding the element and return the final element.
# Now result plays an important role ->  
def allConstruct(target,wordBank,memo={}):
    # if target in memo.keys():
    #     return memo[target]
    if target == "":
        return [[]]
    result = []
    for word in wordBank:
        if target.find(word) == 0:
            sufix = target.replace(word,"")
            sufixWays = allConstruct(sufix,wordBank,memo)
            # targetWays=[]
            for i in sufixWays:
                i.append(word)
                result.append(i)
            memo[target] = result
    print("memo  : ",memo)
    return result
            

print("Result  : ",allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaa",['a','aa','aaa','aaaa','aaaaa']))


# m = target.length
# n= wordBank.length
# -> Result O(n^m) because we are calculating all the possile combination

# space - > O(m)