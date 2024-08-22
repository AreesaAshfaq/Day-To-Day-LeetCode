class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        prev= 0

        for n in nums:
            ans.append(prev + n)
            prev += n
        return ans


        