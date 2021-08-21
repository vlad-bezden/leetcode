class Solution:
    @staticmethod
    def findBuildings(heights: list[int]) -> list[int]:
        result = []
        max_height = 0
        for i in reversed(range(len(heights))):
            if (h := heights[i]) > max_height:
                result.append(i)
                max_height = h
        return sorted(result)


if __name__ == "__main__":
    inputs = (
        ([4, 2, 3, 1], [0, 2, 3]),
        ([4, 3, 2, 1], [0, 1, 2, 3]),
        ([1, 3, 2, 4], [3]),
        ([2, 2, 2, 2], [3]),
    )

    for input, expected in inputs:
        output = Solution.findBuildings(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"
    print("PASSED!!!")
