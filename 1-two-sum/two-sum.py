class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #O(n2)
        for i in range(len(nums)): #O(n)
            for j in range(i+1, len(nums)): #O(n)
                if nums[i] + nums[j] == target: #O(1)
                    return i, j
        
    