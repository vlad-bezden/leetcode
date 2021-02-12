"""206. Reverse Linked List.

Linked list reversed:
1. Iteratively
2. Recursively
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


class Solution:
    @staticmethod
    def to_linked_list(values: list[int]) -> ListNode:
        """Create Linked List of values."""

        head = current_node = ListNode(values[0]) if values else []
        for val in values[1:]:
            current_node.next = ListNode(val)
            current_node = current_node.next
        return head

    @staticmethod
    def to_list(head: ListNode) -> list[int]:
        """Convert Linked List to list."""

        items = []
        start = head
        while start:
            items.append(start.val)
            start = start.next
        return items

    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        """Reverse linked list iteratively."""

        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    @staticmethod
    def recursive_reverse_list(head: ListNode) -> ListNode:
        """Reverse linked list recursively."""

        if not head or not head.next:
            return head
        next_node = head.next
        head.next = None
        new_head = Solution.recursive_reverse_list(next_node)
        next_node.next = head
        return new_head


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 4, 5],
        [10],
        [1, 2],
        [1, 1],
        [],
    ]
    expected = [[5, 4, 3, 2, 1], [10], [2, 1], [1, 1], []]

    for func in [Solution.recursive_reverse_list, Solution.reverseList]:
        for input, expect in zip(inputs, expected):
            print(f"\nProcessing {func.__name__}({input})")
            head = Solution.to_linked_list(input)
            output = Solution.to_list(func(head))
            assert (
                output == expect
            ), f"func: {func.__name__}, {input=}, {expect=}, {output=}"

    print("\nPASSED!!!")
