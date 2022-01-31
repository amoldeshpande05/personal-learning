def gridTraveller(m,n):
    gridArray=[]
    # for i in m+1:
    #     for j in n+1:
    gridArray = [[0] * 4 for _ in range(8)]
    # initialize
    gridArray[1][1] = 1
        
    for i in range(0,len(gridArray)):
        for j in range(0,len(gridArray[0])):
            if (i + 1) < len(gridArray):
                gridArray[i+1][j]+=gridArray[i][j]
            if (j + 1) < len(gridArray[0]):
                gridArray[i][j+1]+=gridArray[i][j]
                   
    print("gridArray  : ",gridArray)
    
    return gridArray[m][n]


print(gridTraveller(3,7))