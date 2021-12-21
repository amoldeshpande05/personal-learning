# [2,3,4,5,6]

def max_sum_subarray(arr,k):
    start = 0
    max_sum = float('-inf')
    curr_sum = 0
    for end, val in enumerate(arr):
        curr_sum+=val
        if (end - start)+1 == k:
            max_sum = max(curr_sum,max_sum)
            curr_sum -= arr[start]
            start+=1
    return max_sum
            
           
arr = [2,3,4,1,5] 
k = 3

print("expected  : 10")
print("actual : ", max_sum_subarray(arr,k))
        
        
        
        
