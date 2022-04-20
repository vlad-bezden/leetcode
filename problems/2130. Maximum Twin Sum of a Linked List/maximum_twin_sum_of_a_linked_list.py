"""2130. Maximum Twin Sum of a Linked List

Level: Medium

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def pairSum_1(head: Optional[ListNode]) -> int:
        """Using list to load data.

        Speed complexity 0(n)
        Memory complexity 0(2n)
        """
        ll_vals = []
        result = 0

        while head:
            ll_vals.append(head.val)
            head = head.next

        for i in range(len(ll_vals) // 2):
            result = max(result, (ll_vals[i] + ll_vals[-1 - i]))

        return result

    @staticmethod
    def pairSum_2(head: Optional[ListNode]) -> int:
        """Using two pointers.

        Run to the middle of the LL and the same time
        reverse first part LL. Then from the middle of LL
        use both pointers to take values one forward and second
        backward.
        """
        prev, slow, fast = None, head, head
        result = 0

        while fast and fast.next:
            fast = fast.next.next
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_

        while slow:
            result = max(result, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return result
