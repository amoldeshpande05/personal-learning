# 1 1 2 3 5 7 13
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

        
        
        