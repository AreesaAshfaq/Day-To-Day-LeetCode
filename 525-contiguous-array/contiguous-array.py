class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0

        diffIndex = {} #count[1] - count[0] = index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            
            if one - zero not in diffIndex:
                diffIndex[one - zero] = i
            if one == zero:
                res = one + zero 
            else: 
                idx = diffIndex[one - zero]
                res = max(res, i - idx)
        
        return res 

        

