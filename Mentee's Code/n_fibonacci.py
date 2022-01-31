def fibonacci_series(n):
    if n == 0:
        return None
    if n == 1:
        return [0]
    # 1D List Initialization
    series=[0]*n
    series[0] = 0
    series[1] = 1
    for i in range(2, n):
        series[i] = series[i-1] + series[i-2]
    return series[n-1]


#   time complexity : O(n)
#   Space Complexity: O(n)


print("The Fibonacci series till n is   : ",fibonacci_series(10))
