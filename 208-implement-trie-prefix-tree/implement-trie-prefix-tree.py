# Complexity Analysis:
#
# Let L = length of the word/prefix.
#
# insert(word):
# Time Complexity: O(L)
# - The loop "for ch in word" visits each character once.
# - Each Trie node lookup/insertion using the dictionary is O(1) on average.
#
# Space Complexity: O(L)
# - In the worst case, each character creates a new Trie node.
#
#
# search(word):
# Time Complexity: O(L)
# - The loop "for ch in word" traverses the Trie one character at a time.
# - Each character lookup in node.children is O(1) on average.
#
# Space Complexity: O(1)
# - Only the pointer "node" is used.
# - No new Trie nodes or extra data structures are created.
#
#
# startsWith(prefix):
# Time Complexity: O(L)
# - The loop "for ch in prefix" traverses each prefix character once.
#
# Space Complexity: O(1)
# - Only the pointer "node" is used.
#
#
# Overall Trie Storage:
# Space Complexity: O(T)
# - T is the total number of unique characters stored in the Trie.

class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False
        

    def insert(self, word: str) -> None:
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()

            node = node.children[ch]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self   

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self   

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]     

        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)