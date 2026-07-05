class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def _compute_hash(self, key: int) -> int:
        return key%10000

    def __init__(self):
        self.h = [Node(-1, -1)]*10000

    def put(self, key: int, value: int) -> None:
        hkey = self._compute_hash(key)
        head = self.h[hkey]
        update = False
        perv = None
        while head:
            if head.key == key:
                head.val = value
                update = True
            prev = head
            head = head.next
        if update == False:
            prev.next = Node(key, value)


    def get(self, key: int) -> int:
        hkey = self._compute_hash(key)
        head = self.h[hkey]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        hkey = self._compute_hash(key)
        head = self.h[hkey]
        perv = None
        found = False
        while head:
            if head.key == key:
                found = True
                break
            prev = head
            head = head.next
        if found:
            prev.next = prev.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)