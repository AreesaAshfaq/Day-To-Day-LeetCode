class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        c = 0
        for i in s[::-1]:
            if i.isspace(): 
                if c != 0:
                    break
            else:
                 c += 1
        return c