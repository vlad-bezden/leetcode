"""113. Path Sum II.

https://leetcode.com/problems/path-sum-ii/
"""

from libs.binary_tree import TreeNode, to_tree


class Solution:
    @staticmethod
    def pathSum(root: TreeNode, target: int) -> list[list[int]]:
        answer = []

        def dfs(node: TreeNode, current_path: list[int], current_target: int) -> None:
            # base case
            if not node:
                return
            # calculate new target
            current_target -= node.val

            if node.left is None and node.right is None and current_target == 0:
                # leaf node and has target value. Solution found.
                answer.append(current_path + [node.val])
            else:
                dfs(node.left, current_path + [node.val], current_target)
                dfs(node.right, current_path + [node.val], current_target)

        dfs(root, [], target)
        return answer


if __name__ == "__main__":
    inputs = (
        (
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1], 22),
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        ),
        (([1, 2, 3], 5), []),
    )

    for input, expected in inputs:
        output = Solution.pathSum(to_tree(input[0]), input[1])
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
