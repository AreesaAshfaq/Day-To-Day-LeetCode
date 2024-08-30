class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        start, last = 1, x

        while start <= last:
            mid = (start + last)//2

            if mid == x // mid:
                return mid
            
            elif mid > x // mid:
                last = mid - 1
            else:
                start = mid + 1
        
        return last