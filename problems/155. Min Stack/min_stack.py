"""155. Min Stack.

Level: Easy

https://leetcode.com/problems/min-stack/
"""
from typing import NamedTuple


class Value(NamedTuple):
    val: int
    min_val: int


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = min(val, self.stack[-1].min_val if self.stack else val)
        self.stack.append(Value(val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min_val
