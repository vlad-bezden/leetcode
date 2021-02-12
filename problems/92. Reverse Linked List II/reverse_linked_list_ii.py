"""92. Reverse Linked List II."""


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
    def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
        """Reverse a linked list from position m to n."""

        # validate for if LL has at least one item
        # and n is greater than 0
        # and n is less than m
        if not head or not head.next or n <= 1 or n <= m:
            return head

        prev = None
        curr = head
        counter = 1

        # find node equal m index
        while counter < m:
            prev = curr
            curr = curr.next
            counter += 1

        tail = curr
        before_m = prev
        # reverse LL section between m and n
        while counter <= n:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            counter += 1
        # remap rest LL and before_m nodes to reversed LL
        tail.next = curr
        if before_m:
            before_m.next = prev
        else:
            head = prev
        return head


if __name__ == "__main__":
    inputs = [
        [[1, 2, 3, 4, 5, 6, 7, 8], 2, 5],
        [[1, 2, 3, 4, 5], 3, 5],
        [[1, 2, 3, 4, 5], 1, 3],
        [[1, 2, 3, 4, 5], 1, 5],
        [[10], 1, 1],
        [[1, 2], 1, 2],
        [[], 1, 2],
    ]
    expected = [
        [1, 5, 4, 3, 2, 6, 7, 8],
        [1, 2, 5, 4, 3],
        [3, 2, 1, 4, 5],
        [5, 4, 3, 2, 1],
        [10],
        [2, 1],
        [],
    ]

    for input, expect in zip(inputs, expected):
        print(f"\nProcessing: {input}")
        head = Solution.to_linked_list(input[0])
        output = Solution.to_list(Solution.reverseBetween(head, *input[1:]))
        assert output == expect, f"{input=}, {expect=}, {output=}"

    print("\nPASSED!!!")
