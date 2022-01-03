# Write a function 'best(targetSum,numbers)' that takes in targetSum and an array of numbers as arguments.
# Return list of elements containing shortest combination of numbers that add up to exactly the target sum
#  You may use a same element as many times as needed
#  All the inputs are non negative

# shortCombination = None
# finalNumbers = []
# def bestSum(targetSum,numbers):
#     shortCombination = None
#     global finalNumbers
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None
    
#     for num in numbers:
#         reminder = targetSum - num
#         result = bestSum(reminder,numbers)
        
#         if result != None:
#             combination = result + [num]
#             if shortCombination == None or len(shortCombination) > len(combination):
#                 shortCombination = combination

#     return shortCombination


# print(bestSum(7,[5,3,4,7]))#True
# print(bestSum(8,[2,3,5]))#True
# print(bestSum(8,[1,4,5]))#True
# print(bestSum(100,[1,2,5,25]))#True



# This approach is amazing, in all the previous programs, like how sum and target sum, we used to stop it as soon as we get the result, and we were not giving chance to run the 2nd for loop from the first recursion call, so our return statement was inside the for loop, now there is no return statement inside the for loop, it will execute for all the combination, and we have an approach of calculating the shortest length sum by maintaing the variable which will keep on executing when the element is found and stores the shortest result



# Now to make it more effecient, use the memorization technique
# The Program goes like this


shortCombination = None
finalNumbers = []
memo = {}
def bestSum(targetSum,numbers):
    shortCombination = None
    global finalNumbers
    global memo
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for num in numbers:
        reminder = targetSum - num
        if reminder in memo.keys():
            result = memo[reminder]
        else:
            result = bestSum(reminder,numbers)
            memo[reminder] = result
            
        
        if result != None:
            combination = result + [num]
            if shortCombination == None or len(shortCombination) > len(combination):
                shortCombination = combination

    memo[targetSum] = shortCombination
    return shortCombination




# Time complexity
#  m  = TargetSum
#  n = len(numbers)

# Brute Force
# time O(n^m)
# Space : O(m^2)  - 1 is recurssion memory 2 is shortestCombination variable for storing array as we recurse


# Memorization
# time O(m*n)
# time O(m^2)