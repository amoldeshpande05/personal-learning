# Return 
[[(2,3),(1,3),(2,4),]]



def bestPathGrid(m,n):
    if m == 1 and n == 1:
        return [[]]
    if m == 0 or n == 0:
        return False
    result = []

    LtupleStore = bestPathGrid(m-1,n)
    RtupleStore = bestPathGrid(m,n-1)
        
    if  LtupleStore!= False:
        for i in LtupleStore:
            i.append((m,n))
            result.append(i)
            
    if  RtupleStore!= False:
        for i in RtupleStore:
            i.append((m,n))
            result.append(i)
    return result
        # Left sub tree values
        
        
print(bestPathGrid(7,7))


# 1 1 1
# 1 1 1
