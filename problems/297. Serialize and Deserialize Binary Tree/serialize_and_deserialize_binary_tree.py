"""297. Serialize and Deserialize Binary Tree"""

from __future__ import annotations
from dataclasses import dataclass
from collections import deque


@dataclass
class TreeNode:
    val: int
    left: TreeNode = None
    right: TreeNode = None


def to_binary_tree(items: list[int]) -> TreeNode:
    """Creates BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build the tree."""
        if n <= index or items[index] is None:
            return None

        return TreeNode(items[index], inner(2 * index + 1), inner(2 * index + 2))

    return inner()


class Codec:
    SEP = ","

    @staticmethod
    def serialize(root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return

        return (
            f"{root.val}{Codec.SEP}"
            f"{Codec.serialize(root.left)}{Codec.SEP}"
            f"{Codec.serialize(root.right)}"
        )

    @staticmethod
    def deserialize(data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return []
        node_values = deque(data.split(Codec.SEP))

        def inner():
            if (val := node_values.popleft()) == "None":
                return None
            return TreeNode(int(val), inner(), inner())

        return inner()


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, None, None, 4, 5, None, None, None, None, None, None, None, 6],
        [1, 2, 5, 3, 4],
        [1, 2, 3, None, None, 4, 5],
        [1, 2, 3, 4, None, None, 5],
        [],
        [1],
        [1, 2],
    ]

    for input in inputs:
        root = to_binary_tree(input)
        ser = Codec.serialize(root)
        output = Codec.deserialize(ser)
        assert ser == Codec.serialize(output), f"{input=}, {output=}"

    print("\nPASSED!!!")
