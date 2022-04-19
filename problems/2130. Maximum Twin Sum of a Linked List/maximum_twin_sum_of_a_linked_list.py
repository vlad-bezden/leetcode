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
    def pairSum(head: Optional[ListNode]) -> int:
        ll_vals = []
        result = 0

        while head:
            ll_vals.append(head.val)
            head = head.next

        for i in range(len(ll_vals) // 2):
            result = max(result, (ll_vals[i] + ll_vals[-1 - i]))

        return result
