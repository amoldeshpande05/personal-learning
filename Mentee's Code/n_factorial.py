def Factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Time O(n)
# Space O(1)
print("The factorial of a number is: ", Factorial(6))

# -> 10/10