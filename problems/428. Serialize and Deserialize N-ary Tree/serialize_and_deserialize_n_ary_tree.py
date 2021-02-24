"""428. Serialize and Deserialize N-ary Tree"""

from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    children: Optional[list[Node]] = None

    def __str__(self):
        return str(self.val)


class Codec:
    SEP = ","

    @staticmethod
    def serialize(root: Optional[Node]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return None

        ans = []

        def inner(node: Node) -> None:
            ans.append(str(node.val))
            for child in node.children:
                ans.append(Codec.SEP)
                inner(child)
            ans.append(Codec.SEP)

        inner(root)
        return "".join(ans)

    @staticmethod
    def deserialize(data: str) -> Optional[Node]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        tokens = deque(data.split(Codec.SEP))

        def inner() -> Optional[Node]:
            if not (val := tokens.popleft()):
                return None
            node = Node(int(val), [])
            while (child := inner()) :
                node.children.append(child)
            return node

        return inner()


if __name__ == "__main__":
    inputs = ["1,3,5,,6,,,2,,4,,", "", "1,2,,3,6,,7,11,14,,,,,4,8,12,,,,5,9,13,,,10,,,"]

    for input in inputs:
        print(f"\nProcession: '{input}'")
        root = Codec.deserialize(input)
        ser = Codec.serialize(root)
        output = Codec.deserialize(ser)
        assert ser == Codec.serialize(output), f"{input=}, {ser=}, {output=}"

    print("\nPASSED!!!")
