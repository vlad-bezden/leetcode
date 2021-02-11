"""234. Palindrome Linked List"""


from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, values: list[int]):
        self.head = prev_node = ListNode(values[0]) if values else ListNode(None)
        for v in values[1:]:
            prev_node.next = ListNode(v)
            prev_node = prev_node.next

    def isPalindrome_3(self, head: ListNode) -> bool:
        """
        Collect values to the end of LL, then compare values with
        reverse list of collected values

        Time complexity O(n), space complexity O(n)
        """

        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

    def isPalindrome_2(self, head: ListNode) -> bool:
        """
        Collecting values to the middle of LL
        and then compare values with the second half of LL.

        Time complexity O(n), space complexity O(n)
        """
        stack = []
        i = 0
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            i += 1
        if i % 2 == 0:
            slow = slow.next
        while stack and (item := stack.pop()):
            if slow.val != item:
                return False
            slow = slow.next
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        """
        Find middle of the LL, reverse first part of the LL
        and traverse both first part in reverse with second part of LL.

        Time complexity O(n), space complexity O(1)
        """
        
        if not head or not head.next:
            return True
        # find middle node of the linked list
        middle_pointer, is_even = self._get_middle(head)
        second_half_pointer = middle_pointer
        if not is_even:
            second_half_pointer = second_half_pointer.next
        # reverse first half of the LL and get pointer to it
        first_half_reverse_pointer = self._reverse_list(head, middle_pointer)
        while first_half_reverse_pointer and second_half_pointer:
            if first_half_reverse_pointer.val != second_half_pointer.val:
                return False
            first_half_reverse_pointer = first_half_reverse_pointer.next
            second_half_pointer = second_half_pointer.next
        return True

    @staticmethod
    def _reverse_list(head: ListNode, up_to_node: ListNode) -> ListNode:
        """Reverse link list.

        1->2->3->4 to 1<-2<-3<-4
        """

        prev = None
        current = head
        while current and current != up_to_node:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    @staticmethod
    def _get_middle(head) -> Tuple[ListNode, bool]:
        """Finds middle node of the Linked List and if LL is even"""

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow, False if fast else True


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 3, 2, 1],
        [10],
        [1, 2],
        [1, 2, 1, 1],
        [1, 2, 3, 1, 2],
        [1, 1],
        [],
    ]
    expected = [False, True, True, True, False, False, False, True, True]

    for input, expect in zip(inputs, expected):
        s = Solution(input)
        print(f"\nProcessing {input}")
        output = s.isPalindrome(s.head)
        assert output == expect, f"{input=}, {expect=}, {output=}"

    print("\nPASSED!!!")
