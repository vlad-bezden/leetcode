"""42. Trapping Rain Water"""


class Solution:
    @staticmethod
    def trap_brute_force(heights: list[int]) -> int:
        """Using brute force

        For each element in the array find the maximum level of
        water it can trap after the rain, which is equal to the minimum
        of maximum height of bars on both the sides minus its own height.

        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        if len(heights) <= 2:
            return 0

        answer = 0
        for i, height in enumerate(heights):
            left_max = right_max = 0
            for h in heights[: i + 1]:
                left_max = max(left_max, h)
            for h in heights[i:]:
                right_max = max(right_max, h)
            answer += min(left_max, right_max) - height

        return answer

    @staticmethod
    def trap_dp(heights: list[int]) -> int:
        """Using dynamic programing

        Find maximum height of bar from the left end up to an index i
            in the array left_max
        Find maximum height of bar from the right end up to an index i
            in the array right_max
        Iterate over the height array and update ans:
            Add min(left_max[i],right_max[i]) - height[i] to ans

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if len(heights) <= 2:
            return 0

        n = len(heights)
        left_max = [0] * n
        right_max = [0] * n
        answer = 0
        # find max hight at each x point on the left and the right side
        for i, h in enumerate(heights):
            left_max[i] = max(*heights[: i + 1], h)
            right_max[i] = max(*heights[i:], h)
        # find the trapped water at each point and add it to the answer
        for i, h in enumerate(heights):
            answer += min(left_max[i], right_max[i]) - h
        return answer

    @staticmethod
    def trap(heights: list[int]) -> int:
        """Using stack

        Time complexity: 0(n)
        Space complexity: 0(n)
        """
        answer = 0
        stack = []
        for i, height in enumerate(heights):
            # check if there is formed container
            while stack and stack[-1][0] < height:
                popped, _ = stack.pop()
                # is it a container though? We have a left border?
                if stack:
                    left_border, j = stack[-1]
                    answer += min(left_border - popped, height - popped) * (i - j - 1)
            stack.append((height, i))
        return answer


if __name__ == "__main__":
    inputs = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 0, 3, 2, 5]]
    expected = [6, 9]

    for input, expect in zip(inputs, expected):
        output = Solution.trap(input)
        assert output == expect, f"{input=}, {output=}, {expect=}"

    print("\nPASSED")
