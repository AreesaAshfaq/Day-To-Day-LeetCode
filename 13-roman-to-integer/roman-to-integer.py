class Solution:
    def romanToInt(self, s: str) -> int:
        romanDic = {"I": 1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        total = 0

        for r in range(len(s)):
            if r != len(s)-1 and romanDic[s[r]] < romanDic[s[r+1]]:
                total -= romanDic[s[r]]
            else:
                total += romanDic[s[r]]
        return total


        