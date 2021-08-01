from typing import Iterable, Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)


def to_tree(items: Iterable[Optional[int]]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree."""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def to_bfs_list(root: Optional[TreeNode]) -> Iterable[Optional[int]]:
    """Convert Tree to list.

    This list is leetcode specific, since it doesn't show None values of the
    leaf node (node that has both left and right nodes None)
    """
    result = []
    this_level = [root]
    while this_level:
        next_level = []
        for n in this_level:
            result.append(n.val if n else None)
            if n and (n.left or n.right):
                next_level.append(n.left)
                next_level.append(n.right)
        this_level = next_level
    return result
