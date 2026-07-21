class MyHashMap:

    def __init__(self):
        self.mp = [-1]*int(1009)


    def put(self, key: int, value: int) -> None:
        self.mp[key%1009] = value

    def get(self, key: int) -> int:
        return self.mp[key%1009]

    def remove(self, key: int) -> None:
        self.mp[key%1009] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)