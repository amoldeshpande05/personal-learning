def fibo_nth_sum(n):
    fiboSeries=[0]*(n+1)
    fiboSeries[1] = 1
    
    for i in range(2,n+1):
        fiboSeries[i] = fiboSeries[i-1]+fiboSeries[i-2]
    return fiboSeries[n]
print(fibo_nth_sum(50))