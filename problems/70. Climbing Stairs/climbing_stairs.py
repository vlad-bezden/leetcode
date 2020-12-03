class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            current = previous = 1
            for _ in range(2, n + 1):
                previous, current = current, current + previous
            return current
