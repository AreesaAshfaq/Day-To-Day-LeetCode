class Solution:
    def reverseVowels(self, s: str) -> str:
        newStr = list(s)
        l = 0
        r = len(s)-1

        while l < r:
            
            if newStr[l].lower() not in ('a', 'e', 'i', 'o', 'u'):
                l += 1
            elif newStr[r].lower() not in ('a', 'e', 'i', 'o', 'u'):
                r -= 1
            else:
                newStr[l], newStr[r] = newStr[r], newStr[l]
                l += 1
                r -= 1

        return "".join(newStr)