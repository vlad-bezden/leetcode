class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"val={self.val} next={self.next.val}"

    def __str__(self):
        return f"val={self.val}"


def to_linked_list(array: list[int]) -> ListNode:
    if not array:
        return array
    root = next_node = ListNode(array[0])
    for i in array[1:]:
        next_node.next = ListNode(i)
        next_node = next_node.next
    return root


def to_list(root: ListNode) -> list[int]:
    answer = []
    while root:
        answer.append(root.val)
        root = root.next
    return answer
