class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) == num.count(str(i)):
                continue
            else:
                return False
        return True
