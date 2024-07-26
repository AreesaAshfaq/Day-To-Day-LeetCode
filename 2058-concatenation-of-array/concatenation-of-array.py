class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Approach 1
        #return nums + nums

        #Approach 2
        # ans = []
        # for i in range(2):
        #     for j in nums:
        #         ans.append(j)
        # return ans

        #Approach 3
        size = 2*len(nums)
        ans = [None]*size
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans

        