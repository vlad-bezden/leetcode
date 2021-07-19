"""Reverse Nodes in k-Group.

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3818/

    Algorithm:
        * Get nodes for this k
        * Check if k-group has less elements than k, and if not, that means group is
            not full and we should leave rest nodes as it's
        * Change values inplace
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        nodes = []
        node = self
        while node:
            nodes.append(str(node.val))
            node = node.next
        return ", ".join(nodes)

    def __repr__(self):
        return str(self.val)


class Solution:
    @staticmethod
    def reverseKGroup(head: ListNode, k: int) -> ListNode:
        curr_node = head
        prev_node = None
        k_group = []
        while curr_node:
            for _ in range(k):
                k_group.append(curr_node)
                curr_node = curr_node.next
                if not curr_node:
                    break
            if len(k_group) < k:
                break
            last_node = k_group[-1]
            node = k_group.pop()
            while k_group:
                temp = k_group.pop()
                node.next = temp
                node = temp
            temp.next = curr_node
            if prev_node:
                prev_node.next = last_node
            else:
                head = last_node
            prev_node = node

        return head


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
