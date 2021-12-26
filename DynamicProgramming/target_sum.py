# Write a function 'canSum(targetSum,numbers)' that takes in targetSum and an array of numbers as argument   
# Return boolean if found or not found
#  You may use a same element as many times as needed
#  All the inputs are non negative
totalSum = 0
memo = {}
def canSum(targetSum,numbers):
    global totalSum
    global memo
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers:
        rem = targetSum - i
        if rem in memo.keys():
            return memo[rem]
        if canSum(rem,numbers):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(8,[2,3,5]))#True
# print(memo)
# memo = {}
# print(canSum(7,[5,3,4,7]))#True
# memo = {}
# print(canSum(7,[2,4]))#False
# memo = {}
# print(canSum(8,[2,3,5]))#True
# memo = {}

# print(canSum(300,[7,14]))#False
