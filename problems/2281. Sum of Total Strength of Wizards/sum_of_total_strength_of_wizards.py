"""2281. Sum of Total Strength of Wizards.

Level: Hard

https://leetcode.com/problems/sum-of-total-strength-of-wizards/
"""


MODULO = 10**9 + 7


from itertools import accumulate


class Solution:
    @staticmethod
    def totalStrength(strength: list[int]) -> int:
        n = len(strength)

        # next small on the right
        right = [n] * n
        stack = []
        for i, v in enumerate(strength):
            while stack and strength[stack[-1]] > v:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left
        left = [-1] * n
        stack = []
        for i, v in reversed(list(enumerate(strength))):
            while stack and strength[stack[-1]] >= v:
                left[stack.pop()] = i
            stack.append(i)

        # for each strength[i] as minimum, calculate sum
        total = 0
        acc = list(accumulate(accumulate(strength), initial=0))
        for i, (l, r, s) in enumerate(zip(left, right, strength)):
            left_acc = acc[i] - acc[max(l, 0)]
            right_acc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            total += s * (right_acc * ln - left_acc * rn)
        return total % MODULO


if __name__ == "__main__":
    tests = (
        ([1, 3, 1, 2], 44),
        ([5, 4, 6], 213),
        ([3], 9),
    )
    for test in tests:
        input, expected = test
        output = Solution.totalStrength(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
