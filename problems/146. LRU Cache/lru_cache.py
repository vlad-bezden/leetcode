"""146. LRU Cache.

https://leetcode.com/problems/lru-cache/
"""

from collections import OrderedDict

NO_KEY_FOUND = -1


class LRUCache:
    def __init__(self, capacity: int):
        self._data = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        result = self._data.get(key, NO_KEY_FOUND)
        if result != NO_KEY_FOUND:
            self._data.move_to_end(key)
        return result

    def put(self, key: int, value: int) -> None:
        if key in self._data:
            self._data[key] = value
            self._data.move_to_end(key)
        elif len(self._data) >= self._capacity:
            self._data.popitem(last=False)
        self._data[key] = value


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
