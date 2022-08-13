"""2. Add Two Numbers.

Level: Medium

https://leetcode.com/problems/add-two-numbers/
"""


from typing import Optional

from libs import linked_list as ll


class Solution:
    @staticmethod
    def addTwoNumbers(
        l1: Optional[ll.ListNode], l2: Optional[ll.ListNode]
    ) -> Optional[ll.ListNode]:
        head = tail = ll.ListNode()
        carry = 0

        while l1 or l2 or carry:
            carry, v = divmod(
                ((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry), 10
            )
            tail.next = ll.ListNode(v)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


if __name__ == "__main__":
    tests = (
        (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
        (([0], [0]), [0]),
        (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
    )
    for test in tests:
        input, expected = test
        output = Solution.addTwoNumbers(
            ll.to_linked_list(input[0]), ll.to_linked_list(input[1])
        )
        result = ll.to_list(output)
        assert result == expected, f"{input =}, {result =}, {expected =}"

    print("PASSED!!!")
