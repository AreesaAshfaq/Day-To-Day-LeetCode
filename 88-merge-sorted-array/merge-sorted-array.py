class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        
        for i in nums2:
            pos = len(nums1) - n
            nums1[pos] = i
            n -= 1

        l, r = 0, 1
        while r != len(nums1):
            if nums1[l] > nums1[r]:
               nums1[l], nums1[r] = nums1[r], nums1[l]
            if nums1[l] == nums1[r]:
                nums1[l+1], nums1[r] = nums1[r], nums1[l+1]
            r += 1
            if r == len(nums1) and l<len(nums1):
                l += 1
                r = l+1 





            


