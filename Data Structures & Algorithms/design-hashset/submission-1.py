class MyHashSet:

    def __init__(self):
        self.keys =[[] for _ in range(1000)]


    def add(self, key: int) -> None:
        if key not in self.keys[key % 1000]:
            self.keys[key % 1000].append(key)

    def remove(self, key: int) -> None:
        if key in self.keys[key% 1000]:
            self.keys[key% 1000].remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.keys[key % 1000] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)