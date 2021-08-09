"""21. Merge Two Sorted Lists.

https://leetcode.com/problems/merge-two-sorted-lists/
"""
from libs.linked_list import ListNode, to_linked_list, to_list


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        answer = head = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return answer.next


if __name__ == "__main__":
    inputs = (
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([], [0]), [0]),
        (([1, 6, 10], [2, 10, 15, 20, 21]), [1, 2, 6, 10, 10, 15, 20, 21]),
        (([1, 4, 6, 8], [2, 5]), [1, 2, 4, 5, 6, 8]),
    )
    for input, expected in inputs:
        ll_1 = to_linked_list(input[0])
        ll_2 = to_linked_list(input[1])
        output = to_list(Solution.mergeTwoLists(ll_1, ll_2))
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
