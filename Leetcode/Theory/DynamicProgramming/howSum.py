# Write a function 'howSum(targetSum,numbers)' that takes in targetSum and an array of numbers as argument   
# Return list of elements that adds up to the target result
#  You may use a same element as many times as needed
#  All the inputs are non negative


finalNumbers = []
def howSum(targetSum,numbers):
    global finalNumbers
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in numbers:
        reminder = targetSum - num
        result = howSum(reminder,numbers)
        if result:
            finalNumbers.append(num)
            return finalNumbers
        

print(howSum(8,[2,3,5,1]))

# time: O(n^m)
    
# print(howSum(300,[7,14]))



# Memorization


# finalNumbers = {}
# memo = {}
# def howSum(targetSum,numbers):
#     global finalNumbers
#     global memo
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None
    
#     for num in numbers:
#         reminder = targetSum - num
#         result = howSum(reminder,numbers)
#         if result != None:
#             finalNumbers[targetSum]= result + [num]
#             return finalNumbers[targetSum]
#     finalNumbers[targetSum] = None
#     return finalNumbers[targetSum]
# time: O(n^m)
    




# m = target sum
# n = number of array element