def max_sum_subarray(arr,s): 
    minSize = float('inf')
    currSum = 0
    start = 0

    for end, val in enumerate(arr):
        currSum += val
        while currSum >= s:
            minSize = min(end-start+1,minSize)
            currSum -= arr[start]
            start+=1
            
    return minSize
            
    
print(max_sum_subarray([2,4,2,5,1],7))
    
    



