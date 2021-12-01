# https://leetcode.com/problems/longest-palindromic-substring/

# Solved by a very time consuming method where you start from the begining and keep on comparing all the other elements with the time complexity of O(n^2) which is executing for all the basic test case, but for the large test case it is throwing time limit exceeded. Exploring other better performing methods.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest = float("-inf")
        finalString=""
        currString = ""   
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                currString = s[i]+s[i+1:j+1]
                print(currString)
                if currString[::-1] == currString and len(currString)>largest:
                    largest = len(currString)
                    finalString = currString
        if not finalString:
            return s[0]
        return finalString
