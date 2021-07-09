"""236. Lowest Common Ancestor of a Binary Tree"""


from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.val=}, {self.left=}, {self.right=}"

    def __repr__(self) -> str:
        return self.__str__()


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if not root:
            return None

        if root in (p, q):
            return root

        # for each root node find left node and right recursive
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if left_res and right_res:
            # both left and right have a and b so this is the LCA node
            return root
        else:
            # a and b are on one side, so only one LCA is available and returned
            return left_res or right_res


if __name__ == "__main__":
    node_2 = TreeNode(2)
    node_6 = TreeNode(6)
    node_9 = TreeNode(9)
    node_9.left = node_2
    node_9.right = node_6
    node_4 = TreeNode(4)
    node_7 = TreeNode(7)
    node_7.right = node_4
    node_3 = TreeNode(3)
    node_3.left = node_9
    node_3.right = node_7
    inputs = [((node_3, node_2, node_6), node_9), ((node_3, node_7, node_6), node_3)]

    s = Solution()
    for input, expected in inputs:
        output = s.lowestCommonAncestor(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
