"""98. Validate Binary Search Tree

    https://leetcode.com/problems/validate-binary-search-tree/

    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:
    * The left subtree of a node contains only nodes with keys less than the node's key.
    * The right subtree of a node contains only nodes with keys greater
        than the node's key.
    * Both the left and right subtrees must also be binary search trees.
"""

from libs.binary_tree import TreeNode, to_binary_tree


class Solution:
    @staticmethod
    def isValidBST(root: TreeNode) -> bool:
        def valid(node: TreeNode, min_: int, max_: int) -> bool:
            if not node:
                return True
            if not min_ < node.val < max_:
                return False
            return valid(node.left, min_, node.val) and valid(
                node.right, node.val, max_
            )

        return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":

    inputs = [
        (to_binary_tree([10, 0, 25, -1, 21, 16, 32]), False),
        (to_binary_tree([10, -10, 19, -20, 0, 17, None]), True),
        (to_binary_tree([2, 1, 3]), True),
        (to_binary_tree([5, 1, 4, None, None, 3, 6]), False),
        (to_binary_tree([2, 2, 2]), False),
        (to_binary_tree([5, 4, 6, None, None, 3, 7]), False),
        (to_binary_tree([3, 1, 5, 0, 2, 4, 6]), True),
    ]

    for input, expected in inputs:
        output = Solution.isValidBST(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
