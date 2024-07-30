class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        w2 = ""

        for c1 in word1:
            w1 += c1
        for c2 in word2:
            w2 += c2

        if w1 == w2:
            return True
        else:
            return False