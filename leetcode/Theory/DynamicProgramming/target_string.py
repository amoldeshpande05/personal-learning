def targetString(targetWord,words,memo={}):
    print(memo)
    if targetWord in memo.keys():
        return memo[targetWord]
    if targetWord == '':
        return True   
     
    for i in words:
        if targetWord.find(i) == 0:
            targetWordtemp = targetWord.replace(i,"")
            if len(targetWordtemp) == len(targetWord):
                continue
            suffix = targetWordtemp
            print(suffix)
            result = targetString(suffix,words,memo)
            if result:
                memo[targetWord]=True
                return True
    memo[targetWord]=False
    return False


print(targetString("enterapotentpots",["a","p","ent","enter","ot","o","t"]))
# print(targetString("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eeee","eeeee","eeeeee","eeeeeee","eeeeeeee"]))


# print(targetString("abab",["abb","abs"]))