def unique_elements_in_list(nums):
    
    # logic to find the unique elements
    temp={}
    result=[]
    for value in nums:
        if value not in temp:
            temp[value]=value
        else:
            temp[value]=False
            
    for i in temp.values():
        if i:
            result.append(i)
    return result

#  Time complexity is : O(2N)
#  Space complexity is : O(N)
def unique_elements_in_list(nums):
    new_list = []
    flag=0
    for i in range(0, len(nums)):
        flag=0
        for j in range(0, len(nums)):
            if i != j:
                if nums[i] == nums[j]:
                    flag=1
                    continue;
        if flag == 0:
            new_list.append(nums[i])
                    
    return new_list

# time complexity: O(n^2)
# Space complexity: O(n)


print("The Unique Elements are:", unique_elements_in_list([3, 2, 3, 4, 6, 6]))


# print("The unique elements are   : ",unique_elements_in_list([3,2,3,4,6,6]))