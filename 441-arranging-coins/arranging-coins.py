class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = n
        res = 0

        while start <= end:
            mid = (start + end)//2
            coins = (mid / 2) * (mid + 1)

            if coins > n:
                end = mid-1
            else:
                start = mid + 1
                res = max(mid, res)
        
        return res