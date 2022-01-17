# My logic is as follows, take first element as a substring, and go on caluclating the same length and matching, if it is not matchins, then run the loop, decrease the array values until you find it, if it is zero then return "" or else return the prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            diff = abs(len(prefix) - len(strs[i]))*-1
            if len(prefix) > len(strs[i]):
                prefix = prefix[:diff]
            if len(prefix) < len(strs[i]):
                strs[i] = strs[i][:diff]
                
            while prefix not in strs[i]:
                prefix=prefix[:-1]
                strs[i]=strs[i][:-1]
            if len(prefix) == 0:
                return ""
        return prefix
        
                
                
        
# Very simple solution, just consider the prefix, and go on reducing it until you find the substring in 0'th position
# while strs[i].find(prefix) != 0:
# Go on reducing
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if prefix == "":
            return ""
        for i in range(1,len(strs)):
            while strs[i].find(prefix) != 0:
                prefix=prefix[:-1]
        return prefix