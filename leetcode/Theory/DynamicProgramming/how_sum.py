# Write a function 'howSum(targetSum,numbers)' that takes in targetSum and an array of numbers as argument   
# Return list of elements that adds up to the target result
#  You may use a same element as many times as needed
#  All the inputs are non negative


def canSum(targetSum,numbers):
    combination = None
    if targetSum == 0:
        return []
    if targetSum < 0:
        return False
   
    for i in numbers:
        rem = targetSum - i
        result = canSum(rem,numbers)
        if result != False:
            combination = result + [i]
            return combination
        
    return combination

print(canSum(12,[3,3,3]))



# def canSum(targetSum,numbers):
#     combination = None
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return False
   
#     for i in numbers:
#         rem = targetSum - i
#         result = canSum(rem,numbers)
#         if result != False:
#             combination = result + [i]
#             return combination
        
#     return combination

# print(canSum(12,[3,3,3]))