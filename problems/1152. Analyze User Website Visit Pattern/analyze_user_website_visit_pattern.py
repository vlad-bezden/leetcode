"""1152. Analyze User Website Visit Pattern.

Level: Medium

https://leetcode.com/problems/analyze-user-website-visit-pattern/
"""

from collections import defaultdict


class Solution:
    @staticmethod
    def mostVisitedPattern(
        usernames: list[str], timestamps: list[int], websites: list[str]
    ) -> list[str]:
        # create triplets sorted by time
        sorted_data = sorted(zip(usernames, timestamps, websites), key=lambda x: x[1])

        formated_data = defaultdict(list)

        # create dict with k=user and v=visited sites
        for u, _, w in sorted_data:
            formated_data[u].append(w)

        pattern = defaultdict(int)

        for u, w in formated_data.items():
            visited = set()

            # create paterns from visited sites
            for i, w1 in enumerate(w[:-2]):
                for j, w2 in enumerate(w[i + 1 : -1], start=i + 1):
                    for w3 in w[j + 1 :]:
                        p = (w1, w2, w3)

                        # count times of visited paterns
                        if p not in visited:
                            visited.add(p)
                            pattern[p] += 1

        max_visited = max(pattern.values())
        keys_with_max_value = [k for k, v in pattern.items() if v == max_visited]

        return list(sorted(keys_with_max_value)[0])


if __name__ == "__main__":
    tests = (
        (
            (
                ["zkiikgv", "zkiikgv", "zkiikgv", "zkiikgv"],
                [436363475, 710406388, 386655081, 797150921],
                ["wnaaxbfhxp", "mryxsjc", "oz", "wlarkzzqht"],
            ),
            ["oz", "mryxsjc", "wlarkzzqht"],
        ),
        (
            (
                ["dowg", "dowg", "dowg"],
                [158931262, 562600350, 148438945],
                ["y", "loedo", "y"],
            ),
            ["y", "y", "loedo"],
        ),
        (
            (
                [
                    "joe",
                    "joe",
                    "joe",
                    "james",
                    "james",
                    "james",
                    "james",
                    "mary",
                    "mary",
                    "mary",
                ],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [
                    "home",
                    "about",
                    "career",
                    "home",
                    "cart",
                    "maps",
                    "home",
                    "home",
                    "about",
                    "career",
                ],
            ),
            ["home", "about", "career"],
        ),
        (
            (
                ["ua", "ua", "ua", "ub", "ub", "ub"],
                [1, 2, 3, 4, 5, 6],
                ["a", "b", "a", "a", "b", "c"],
            ),
            ["a", "b", "a"],
        ),
    )

    for test in tests:
        input, expected = test
        result = Solution.mostVisitedPattern(*input)
        assert result == expected

    print("PASSED!!!")
