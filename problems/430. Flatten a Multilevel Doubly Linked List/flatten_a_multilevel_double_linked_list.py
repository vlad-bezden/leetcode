"""430. Flatten a Multilevel Doubly Linked List."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    prev: Node
    next: Node
    child: Node


class Solution:
    def flatten(self, head: Node) -> Node:
        """Flatten multilevel link list using DFS.

            n - number of nodes
            Time complexity = O(n).
            Space complexity = O(n), number of nodes in the stack
        """
        if not head:
            return head

        stack = [head]
        prev = None

        while stack:
            curr = stack.pop()
            curr.prev = prev
            if prev:
                prev.next = curr
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        return head


def trace(head: Node) -> list[int]:
    answer = []
    while head:
        answer.append(head.val)
        head = head.next
    return answer


if __name__ == "__main__":
    solution = Solution()

    node1 = Node(1, None, None, None)
    node2 = Node(2, node1, None, None)
    node1.next = node2
    node3 = Node(3, node2, None, None)
    node2.next = node3
    node4 = Node(4, node3, None, None)
    node3.next = node4
    node5 = Node(5, node4, None, None)
    node4.next = node5
    node6 = Node(6, node5, None, None)
    node5.next = node6

    node7 = Node(7, None, None, None)
    node3.child = node7
    node8 = Node(8, node7, None, None)
    node7.next = node8
    node9 = Node(9, node8, None, None)
    node8.next = node9
    node10 = Node(10, node9, None, None)
    node9.next = node10

    node11 = Node(11, None, None, None)
    node8.child = node11
    node12 = Node(12, node11, None, None)
    node11.next = node12

    expected = [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

    output = solution.flatten(node1)
    output_values = trace(output)

    assert output_values == expected, f"{expected= }, {output_values= }"

    print("PASSED!!!")
