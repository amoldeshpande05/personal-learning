# Write a function 'canSum(targetSum,numbers)' that takes in targetSum and an array of numbers as argument   
# Return boolean if found or not found
#  You may use a same element as many times as needed
#  All the inputs are non negative


# def canSum(targetSum,numbers):
#     if targetSum == 0:
#         return True
#     if targetSum < 0:
#         return False
#     for i in numbers:
#         rem = targetSum - i
#         if canSum(rem,numbers):
#             return True
#     return False
    
    


# Memorised
memo = {}
def canSum(targetSum,numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers:
        rem = targetSum - i
        if rem in memo.keys():
            return memo[rem]
        if canSum(rem,numbers):
            memo[rem] = True
            return True
    memo[targetSum] = False 
    return False

print(canSum(12,[3,3,3]))