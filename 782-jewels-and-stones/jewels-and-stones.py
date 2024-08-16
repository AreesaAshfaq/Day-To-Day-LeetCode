class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set(jewels)
        count = 0
        for jewel in jewelSet:
            count += stones.count(jewel)
        return count

