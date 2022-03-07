#User function Template for python3

def getMinMax( a, n):
    minimum = a[0]
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] < minimum:
            minimum = a[i]
        if a[i] > maximum:
            maximum = a[i]
    
    return minimum,maximum
            