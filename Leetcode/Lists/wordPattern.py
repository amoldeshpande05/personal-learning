# Take two dict and store both the patterns and then compute

class Solution:
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        way1 = {}
        way2 = {}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        for index,word in enumerate(words):
            if pattern[index] in way1 or word in way2:
                if pattern[index] in way1 and way1[pattern[index]] == word and word in way2 and way2[word] == pattern[index]:
                    continue;
                else:
                    return False
            else:
                way1[pattern[index]]=word
                way2[word]=pattern[index]
        return True
            
          


    
