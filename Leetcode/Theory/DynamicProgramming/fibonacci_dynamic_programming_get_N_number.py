# 1 1 2 3 5 7 13
result = {}
def fibonacci(n):
    if n <= 2:
        return 1
    if n in result.keys():
        return result[n]
    print(n)
    result[n] = fibonacci(n-1) + fibonacci(n-2)
    return result[n]

print(fibonacci(7))
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 2
# 3
# 2
# 1
# 4
# 3
# 2
# 1
# 2
# 5
# 4
# 3
# 2
# 1
# 2
# 3
# 2
# 1
        
        
        