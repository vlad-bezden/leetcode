"""146. LRU Cache.

https://leetcode.com/problems/lru-cache/
"""

from collections import OrderedDict

NO_KEY_FOUND = -1


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._data = OrderedDict()

    def get(self, k: int) -> int:
        v = self._data.get(k, NO_KEY_FOUND)

        if v != NO_KEY_FOUND:
            self._data.move_to_end(k)
        return v

    def put(self, k: int, v: int) -> None:
        if k in self._data:
            self._data.move_to_end(k)
        self._data[k] = v
        if len(self._data) > self._capacity:
            self._data.popitem(last=False)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == NO_KEY_FOUND
    lru.put(4, 4)
    assert lru.get(1) == NO_KEY_FOUND
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    print("PASSED!!!")
