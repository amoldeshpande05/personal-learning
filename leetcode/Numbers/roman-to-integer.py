#  Normal branching approach, based on the description, went on writing the if condition branches based on the condtion specified in the problem statement
# https://leetcode.com/problems/roman-to-integer/submissions/
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        temp = None
        for i in range(len(s)-1,-1,-1):
            if s[i] == 'I' and (temp == 'V' or temp == 'X'):
                total-=1
                flag = 1
            elif s[i] == 'X' and (temp == 'L' or temp == 'C'):
                total -= 10
                flag = 1
            elif s[i] == 'C' and (temp == 'D' or temp == 'M'):
                total -= 100
            else:  
                if s[i] == 'I':
                    total+=1
                if s[i] == 'V':
                    total+=5
                if s[i] == 'X':
                    total+=10
                if s[i] == 'L':
                    total +=50
                if s[i] == 'C':
                    total +=100
                if s[i] == 'D':
                    total+=500
                if s[i] == 'M':
                    total+=1000
            temp = s[i]
                
        return total
                    
                    
# One more approach is that
#  largest to smallest: add them up
#  if a current element is smaller than the next element, substract it
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total
                
         
        