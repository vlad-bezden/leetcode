from collections import deque, namedtuple

point = namedtuple("point", ["index", "value"])


def count_subarrays(arr):
    n = len(arr)
    result = [1] * n

    # left
    stack = deque()
    for i, v in enumerate(arr):
        while stack and stack[-1].value < v:
            stack.pop()
        result[i] += i - stack[-1].index - 1 if stack else i
        stack.append(point(i, v))

    # right
    stack.clear()
    for i, v in enumerate(arr[::-1]):
        while stack and stack[-1].value < v:
            stack.pop()
        result[n - i - 1] += i - stack[-1].index - 1 if stack else i
        stack.append(point(i, v))

    return result


if __name__ == "__main__":
    tests = [
        ([3, 4, 1, 6, 2], [1, 3, 1, 5, 1]),
        ([2, 4, 7, 1, 5, 3], [1, 2, 6, 1, 3, 1]),
        ([3, 6, 4, 1, 5, 2], [1, 6, 2, 1, 4, 1]),
    ]

    for input, expected in tests:
        result = count_subarrays(input)
        assert result == expected, f"{input=}, {result=}, {expected=}"

    print("PASSED!!!")
