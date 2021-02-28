"""449. Serialize and Deserialize BST."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Union
from collections import deque


@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

    def __repr__(self: TreeNode) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"


TreeNodeT = Union[list, TreeNode]


class Codec:
    @staticmethod
    def serialize(root: TreeNodeT) -> str:
        if not root:
            return ""
        values = []

        def dfs(node):
            if node:
                values.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                values.append("")

        dfs(root)
        return ",".join(values)

    @staticmethod
    def deserialize(data: str) -> TreeNodeT:
        if not data:
            return []
        queue = deque(data.split(","))

        def dfs():
            if queue and (val := queue.popleft()):
                return TreeNode(int(val), dfs(), dfs())

        return dfs()


if __name__ == "__main__":
    inputs = ["2,1,,,3,,", "", "6,4,3,,,5,,,10,9,8,,,,11,,"]
    for input in inputs:
        print(f"\nProcessing: '{input}'")
        root = Codec.deserialize(input)
        ser = Codec.serialize(root)
        output = Codec.deserialize(ser)
        assert input == Codec.serialize(output), f"{input=}, {ser=}, {output=}"

    print("\nPASSED!!!")
