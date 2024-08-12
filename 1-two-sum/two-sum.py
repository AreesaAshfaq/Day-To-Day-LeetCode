class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Brute Force Appraoch : O(n2)
       
        # for i in range(len(nums)): #O(n)
        #     for j in range(i+1, len(nums)): #O(n)
        #         if nums[i] + nums[j] == target: #O(1)
        #             return i, j
        
        # Using Two Pointers: O(nlogn)

        numsS = sorted(nums)
        l = 0
        r = len(numsS)-1

        while l < r:
            if numsS[l] + numsS[r] > target:
                r -= 1
            elif numsS[l] + numsS[r] < target:
                l += 1
            else:
                break

        ans = []
        for i in range(len(nums)):
            if nums[i] == numsS[l]:
                ans.append(i)
            elif nums[i] == numsS[r]:
                ans.append(i)

        return ans
        
            

                
        
