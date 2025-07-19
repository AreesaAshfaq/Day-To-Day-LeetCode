class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evenArr = []
        oddArr = []
        for i in nums:
            if i%2 == 0:
                evenArr.append(i)
            else:
                oddArr.append(i)
        return evenArr + oddArr

        