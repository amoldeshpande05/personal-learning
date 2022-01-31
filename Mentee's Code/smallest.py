def smallest(list):
    if len(list) == 0:
        return None
    
    smallest = -99999
    for i in range(0,len(list)):
        if smallest > list[i]:
            smallest = list[i]
    return smallest


print("The smallest element is  : ",smallest([3,2,1,34,55])) 
