# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    s = Solution()

    # Example 1
    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_0 = ListNode(0)
    node_n4 = ListNode(-4)
    node_3.next = node_2
    node_2.next = node_0
    node_0.next = node_n4
    node_n4.next = node_2
    assert s.hasCycle(node_3) is True

    # Example 2
    node_n4.next = None
    assert s.hasCycle(node_3) is False

    # Example 3
    node_1 = ListNode(1)
    node_2.next = node_1
    node_1.next = node_2
    node_2.next = node_1
    assert s.hasCycle(node_1) is True

    # Example 4
    node_2.next = None
    assert s.hasCycle(node_1) is False

    # Example 5
    node_1.next = None
    assert s.hasCycle(node_1) is False

    print("PASSED!!!")
