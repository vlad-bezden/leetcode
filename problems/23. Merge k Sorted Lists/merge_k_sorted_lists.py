"""23. Merge k Sorted Lists.

Level: Hard

https://leetcode.com/problems/merge-k-sorted-lists/
"""

from typing import Optional

from libs.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next


if __name__ == "__main__":
    tests = (
        ([[1, 2], [3, 4], [5, 6], [7, 8]], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([[1, 4, 5], [1, 3, 4], [2, 6, 8]], [1, 1, 2, 3, 4, 4, 5, 6, 8]),
        ([[]], []),
        ([], []),
    )
    solution = Solution()
    for test in tests:
        input, expected = test
        output = solution.mergeKLists([to_linked_list(l) for l in input])
        output = [] if output is None else output
        assert to_list(output) == expected, f"{input = }, {output = }, {expected = }"

    print("PASSED!!!")
