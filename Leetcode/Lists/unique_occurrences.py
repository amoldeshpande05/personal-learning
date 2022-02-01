
# https://leetcode.com/problems/unique-number-of-occurrences/submissions/

# Straight fwd, just store it in a dictionary with the count, and get the values and compare it with set and without set, that will be your answer
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniqueHash={}
        for i in arr:
            if i not in uniqueHash:
                uniqueHash[i]=1
            else:
                uniqueHash[i]+=1
        return len(set(uniqueHash.values())) == len(uniqueHash.values())
           