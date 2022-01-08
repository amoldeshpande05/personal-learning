def targetString(targetWord,words):
    if targetWord == '':
        return True    
    for i in words:
        try: 
            if targetWord.index(i) == 0:
                targetWordtemp = targetWord.replace(i,"")
                if len(targetWordtemp) == len(targetWord):
                    continue
                suffix = targetWordtemp
                print(suffix)
                result = targetString(suffix,words)
                if result:
                    return True
        except:
            continue
    return False


print(targetString("skateboard",["bo","rd","ate","t","ska","sk","boar"]))

# print(targetString("abab",["abb","abs"]))