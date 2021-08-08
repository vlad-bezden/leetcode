"""938. Range Sum of BST

https://leetcode.com/problems/range-sum-of-bst/
"""

from typing import Optional
from libs.binary_tree import TreeNode, to_tree


class Solution:
    @staticmethod
    def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0

        def dfs(node: TreeNode) -> int:
            nonlocal answer
            if node:
                if low <= node.val <= high:
                    answer += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        dfs(root)
        return answer


if __name__ == "__main__":
    inputs = (
        ({"root": [10, 5, 15, 3, 7, None, 18], "low": 7, "high": 15}, 32),
        ({"root": [10, 5, 15, 3, 7, 13, 18, 1, None, 6], "low": 6, "high": 10}, 23),
    )
    for input, expected in inputs:
        input["root"] = to_tree(input["root"])
        output = Solution.rangeSumBST(**input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
