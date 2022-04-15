"""341. Flatten Nested List Iterator.

Level: Medium

https://leetcode.com/problems/flatten-nested-list-iterator/
"""


class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.flat_list = []

        def flatten(data):
            for i in data:
                if i.isInteger():
                    self.flat_list.append(i.getInteger())
                else:
                    flatten(i.getList())

        flatten(nested_list)
        self.index = 0

    def next(self) -> int:
        value = self.flat_list[self.index]
        self.index += 1
        return value

    def hasNext(self) -> bool:
        return self.index < len(self.flat_list)
