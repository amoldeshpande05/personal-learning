class Solution:
        
    def isPalindrome(self, s: str) -> bool:
        finalString=""
        for character in s:
            if character.isalnum():
                finalString += character.lower()
        
        return finalString == finalString[::-1]
        