# Main logic was to compare the binary conversion to decimal, similary covert 26arry to decimal, the problem will be solved


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        for i in range(len(columnTitle)-1,-1,-1):
            result+=(ord(columnTitle[i])-64)* pow(26,len(columnTitle)-i-1)
            count+=1
        return result
         