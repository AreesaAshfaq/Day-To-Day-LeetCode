class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Sum = sum(nums)
        for i in range(len(nums)):
            rem = target - nums[i]
            if (target == rem + nums[i]) and rem in nums and nums.index(rem) != i:
                return [nums.index(rem), i]
        
        