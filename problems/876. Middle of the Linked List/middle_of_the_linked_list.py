"""876. Middle of the Linked List.

    Solution has two approaches.
    1. Using two pointers (fast and slow)
    2. Using dictionary to map all nodes and get median node

    Solution:
        Using two pointers (fast and slow) is about 1.5 - 2 times faster.

    Output:
        Processing [1, 2, 3, 4, 5]
        middleNode took: 0.049111
        middleNode_2 took: 0.092054

        Processing [1, 2, 3, 4, 5, 6]
        middleNode took: 0.063219
        middleNode_2 took: 0.122501

        Processing [10]
        middleNode took: 0.016189
        middleNode_2 took: 0.041323

        Processing [10, 9, 8, 7, 6]
        middleNode took: 0.047844
        middleNode_2 took: 0.095471

        Processing [8, 7]
        middleNode took: 0.029129
        middleNode_2 took: 0.053927

        Processing [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                    19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                    36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                    53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                    70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                    87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        middleNode took: 0.952326
        middleNode_2 took: 1.503520

"""
from timeit import timeit


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, values: list[int]):
        self.head = prev_node = ListNode(values[0])
        for v in values[1:]:
            prev_node.next = ListNode(v)
            prev_node = prev_node.next

    def middleNode(self, head: ListNode) -> ListNode:
        """Using fast and slow pointers."""
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode_2(self, head: ListNode) -> ListNode:
        """Using dict to map index to node and return median node."""
        counter = 0
        mapper = {}
        while head:
            counter += 1
            mapper[counter] = head
            head = head.next
        return mapper[counter // 2 + 1]


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [10],
        [10, 9, 8, 7, 6],
        [8, 7],
        [*range(100)],
    ]
    expected = [3, 4, 10, 8, 7, 50]

    for input, expect in zip(inputs, expected):
        s = Solution(input)
        print(f"\nProcessing {input}")
        for f in [s.middleNode, s.middleNode_2]:
            output = f(s.head).val
            assert output == expect, f"{input=}, {expect=}, {output=}"
            t = timeit(stmt="f(s.head)", number=100_000, globals=globals())
            print(f"{f.__name__} took: {t:.6f}")

    print("\nPASSED!!!")
