def reverseBit(n):
    
    res = 0
    for i in range(0,32):
        bit = (n>>i) & 1
        bit = bit << (31 - i)
        res = res | bit
    return res

# Explaination is as follows, first we need to find the last element, in order to find that, do & 1, we will get last digit. Now once we get the last digit, create a bit, take it at the first(31-i) and then add it to a result, to add we use or
        
    