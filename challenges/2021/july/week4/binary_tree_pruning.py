"""Binary Tree Pruning

    https://leetcode.com/problems/binary-tree-pruning/
"""

from typing import Optional
from libs.binary_tree import to_bfs_list, to_tree, TreeNode


class Solution:
    @staticmethod
    def pruneTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = Solution.pruneTree(root.left)
        root.right = Solution.pruneTree(root.right)
        if root.left or root.right or root.val:
            return root
        return None


if __name__ == "__main__":
    inputs = (
        ([1, None, 0, None, None, 0, 1], [1, None, 0, None, 1]),
        ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
        ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
    )

    for input, expected in inputs:
        output_tree = Solution.pruneTree(to_tree(input))
        output_list = to_bfs_list(output_tree)
        assert output_list == expected, f"{input=}, {output_list=}, {expected=}"

    print("PASSED!!!")
