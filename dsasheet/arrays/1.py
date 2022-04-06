def reverseArray(num):
    
    for i in range(len(num)//2):
        temp = num[i]
        num[i]=num[len(num)-i-1]
        num[len(num)-i-1] = temp
        
    return num


print("reverse String  : ",reverseArray(['1','2',3,4]))
        