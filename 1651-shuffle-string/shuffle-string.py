class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        res = [0]*len(s)

        for c in range(len(s)):
            res[indices[c]] = s[c]
        
        return "".join(res)
        
        

