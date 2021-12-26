# 1,1,2,3,5,8

# Normal For Loop Fibonacci series

l = 1
r = 1
def n_Fibonacii_numbers(n): 
    global l
    global r
    if n == 1:
        return 1
    if n == 2:
        return 1,2
    print(1)
    print(1)
    for i in range(2,n):
        tempSum = l + r
        print(tempSum)
        l=r
        r = tempSum        
n_Fibonacii_numbers(10)

        
    
    