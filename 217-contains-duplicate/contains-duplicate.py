class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Approach 1
        return len(nums) != len(set(nums))

        #Approach 2
        # dic = {}
        # for i in range(len(nums)):
        #     if nums[i] in dic:
        #         return True
        #     else:
        #         dic[nums[i]] = i+1
        # return False
        