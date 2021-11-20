# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

# First approach with list
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = 0
        currStringList = []
        stringList = list(s)
        if len(s) == 1:
            return 1
        for end,val in enumerate(stringList):
            if val in currStringList:
                while val in currStringList:
                    currStringList.pop(0)
            currStringList.append(val)
            maxSize = max(maxSize,len(currStringList))

        return maxSize
            
            
            
#  Second approach is with string itself and no conversion  # Most efficient method

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        maxSize = 0
        currStringList = ""
        for val in s:
            while val in currStringList:
                currStringList = currStringList[1::]
            currStringList+=val
            maxSize = max(maxSize,len(currStringList))
        return maxSize
    
    
#  This is solved based on the approach of sliding window with some modification, don't use any start or end pointer, sliding is done based on untill you find the repeated character, We start scanning each charater and check if the character is present in our currString, if it is then from the begining start removing untill we find the required character, after the while loop, then add the present value. Keep track on the max size of the list
    
            
            
            
        
    
    
    
    
            
            
            
        
    
    
#  Explaination
# This program is solved by the approach known as sliding window, where we start looping through the string, check 
    
            
            
            
        