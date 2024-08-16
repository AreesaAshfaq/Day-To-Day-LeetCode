class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Approach 1: O(n)
        n = len(nums)
        total = (n*(n + 1))/2
        for num in nums:
            total -= num
        return int(total)

        #Approach 2: O(n2)
        # i = 0
        # while i <= len(nums):
        #     if i not in nums:
        #         return i
        #     i += 1


