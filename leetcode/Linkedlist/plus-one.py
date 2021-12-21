# https://leetcode.com/problems/plus-one/submissions/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while digits[i] == 9:
            digits[i] = 0
            i-=1 
        if i != -1:
            digits[i]+=1
        else:
            digits.insert(0,1)
        return digits
    
# Explaination: First go on finding the digit 9 and keep on decrementing it until you find the digit which is not 9, if not 9 then increment it, if it's a first digit, then append 1 in the front

# another one line code
#   num = list(str(int(''.join(str(i) for i in digits)) + 1))
# # return num