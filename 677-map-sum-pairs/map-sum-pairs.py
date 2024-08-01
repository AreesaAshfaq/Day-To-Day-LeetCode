class MapSum:

    def __init__(self):
      self.hashMap = {}

    def insert(self, key: str, val: int) -> None:
        self.hashMap[key] = val

    def sum(self, prefix: str) -> int:
        sum = 0
        for k in self.hashMap:
            if prefix == k[:len(prefix)]:
                sum += self.hashMap[k] 
        return sum     


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)