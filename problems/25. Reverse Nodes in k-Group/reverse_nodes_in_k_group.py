"""Reverse Nodes in k-Group.

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3818/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        nodes = []
        node = self
        while node:
            nodes.append(f"{node!r}")
            node = node.next
        return ", ".join(nodes)

    def __repr__(self):
        return str(self.val)


class Solution:
    @staticmethod
    def reverseKGroup(head: ListNode, k: int) -> ListNode:
        # find last node in k group
        k_group_head = head
        i = 0
        while k_group_head and i < k:
            k_group_head = k_group_head.next
            i += 1
        # check if there are not a full k group
        if i < k:
            return head
        # new head in k-group
        new_k_group_head = Solution.reverseKGroup(k_group_head, k)
        # perform swapping.
        # a->b->c => b->a->c => c->b->a
        # 'a' always points to the start of the chain
        # and 'b' to the next swapping element
        a = head
        b = a.next
        for i in range(k - 1):
            c = b.next
            b.next = a
            # a point to the start of the chain
            a = b
            # b point to the next swapping element
            b = c
        # point head/which is now at the end of the k-list to the next k-group
        head.next = new_k_group_head
        return a


if __name__ == "__main__":

    def create_list(n: int) -> ListNode:
        head = current_node = ListNode(1)
        for i in range(2, n + 1):
            new_node = ListNode(i)
            current_node.next = new_node
            current_node = new_node
        return head

    inputs = (
        [(create_list(5), 3), "3, 2, 1, 4, 5"],
        [(create_list(5), 2), "2, 1, 4, 3, 5"],
        [(create_list(6), 3), "3, 2, 1, 6, 5, 4"],
    )
    for input, expected in inputs:
        output = str(Solution.reverseKGroup(*input))
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
