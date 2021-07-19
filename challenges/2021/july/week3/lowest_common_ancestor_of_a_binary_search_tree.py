"""Lowest Common Ancestor of a Binary Search Tree

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3819/
"""


class TreeNode:
    def __init__(self, x, left=None, right=None) -> None:
        self.val = x
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return f"{self.val=}, {self.left=}, {self.right=}"


class Solution:
    @staticmethod
    def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val < p.val and root.val < q.val:
            # move to the right side of the current node
            return Solution.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            # move to the left of current node
            return Solution.lowestCommonAncestor(root.left, p, q)
        # that is a lowest common ancestor
        return root


if __name__ == "__main__":

    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n3, n5)
    n0 = TreeNode(0)
    n2 = TreeNode(2, n0, n4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n8 = TreeNode(8, n7, n9)
    root = n6 = TreeNode(6, n2, n8)

    inputs = (
        ((root, n2, n8), root),
        ((root, n2, n4), n2),
        ((root, n3, n5), n4),
        ((root, n0, n9), n6),
    )
    for input, expected in inputs:
        output = Solution.lowestCommonAncestor(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
