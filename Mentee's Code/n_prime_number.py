def prime_number(n):
    if n < 2:
        return False
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            return False
    return n

def first_n_PrimeNumbers(n):
    nPrime=[]
    for i in range(0,n):
        primeNumber = prime_number(i)
        if primeNumber != False:
            nPrime.append(prime_number(i))
    
    return nPrime
    
    

# print("The given number is  ",first_n_PrimeNumbers(13))

print(first_n_PrimeNumbers(13))


# 1 2 3 4 5 6 7 8