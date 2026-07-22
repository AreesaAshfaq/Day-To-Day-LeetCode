class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Merge function
        def merge(left, right):
            res = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            # Add remaining elements
            res.extend(left[i:])
            res.extend(right[j:])

            return res
                
        # Merge Sort function
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            # Divide array into two halves
            mid = len(arr)//2

            leftHalf = mergeSort(arr[:mid])
            rightHalf = mergeSort(arr[mid:])

            # Merge sorted halves
            return merge(leftHalf, rightHalf)
        return mergeSort(nums)