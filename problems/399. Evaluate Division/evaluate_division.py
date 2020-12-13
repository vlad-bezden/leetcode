"""Evaluate Division.

    Two methods:
        1. Using recursion
        2. Using backtracking algorithm, or (DFS)

    Output:
        Running calcEquation
        calcEquation took: 0.095297
        calcEquation took: 0.132599
        calcEquation took: 0.074000
        calcEquation took: 0.200761
        calcEquation took: 0.154011

        Running calcEquation_2
        calcEquation_2 took: 0.073487
        calcEquation_2 took: 0.082386
        calcEquation_2 took: 0.041389
        calcEquation_2 took: 0.118606
        calcEquation_2 took: 0.080027

        Running calcEquation
        calcEquation took: 0.092658
        calcEquation took: 0.120047
        calcEquation took: 0.062742
        calcEquation took: 0.181758
        calcEquation took: 0.118967

        Running calcEquation_2
        calcEquation_2 took: 0.057865
        calcEquation_2 took: 0.072529
        calcEquation_2 took: 0.039897
        calcEquation_2 took: 0.115322
        calcEquation_2 took: 0.079738

        Running calcEquation
        calcEquation took: 0.086553
        calcEquation took: 0.117590
        calcEquation took: 0.061209
        calcEquation took: 0.179509
        calcEquation took: 0.114457

        Running calcEquation_2
        calcEquation_2 took: 0.055642
        calcEquation_2 took: 0.080263
        calcEquation_2 took: 0.045806
        calcEquation_2 took: 0.131219
        calcEquation_2 took: 0.076117

        Running calcEquation
        calcEquation took: 0.082799
        calcEquation took: 0.121331
        calcEquation took: 0.063149
        calcEquation took: 0.174963
        calcEquation took: 0.120448

        Running calcEquation_2
        calcEquation_2 took: 0.055546
        calcEquation_2 took: 0.073534
        calcEquation_2 took: 0.039302
        calcEquation_2 took: 0.126678
        calcEquation_2 took: 0.077394

        Running calcEquation
        calcEquation took: 0.081621
        calcEquation took: 0.135562
        calcEquation took: 0.059353
        calcEquation took: 0.182438
        calcEquation took: 0.116120

        Running calcEquation_2
        calcEquation_2 took: 0.054943
        calcEquation_2 took: 0.071296
        calcEquation_2 took: 0.038812
        calcEquation_2 took: 0.114352
        calcEquation_2 took: 0.077203
"""
from timeit import timeit
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        """Using recursion."""
        graph = defaultdict(dict)
        results = []
        # Step 1). build the graph from the equations
        for (dividend, divisor), v in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = v
            graph[divisor][dividend] = 1 / v

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        for c, d in queries:
            if c not in graph or d not in graph:
                # case 1): either node does not exist
                results.append(-1)
            elif c == d:
                # case 2): origin and destination are the same node
                results.append(1)
            else:
                results.append(Solution._path(graph, c, d))
        return results

    @staticmethod
    def _path(graph: dict, start: str, end: str) -> float:
        def calculate(start, end, visited):
            visited.add(start)
            for k, v in (i for i in graph[start].items() if i[0] not in visited):
                if end == k:
                    return v
                if (result := calculate(k, end, visited)) and result != -1:
                    return v * result
            return -1

        return calculate(start, end, set())

    def calcEquation_2(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        """Using backtracking algorithm.

        Or sometimes it's called DFS (Depth-First Search).
        """
        graph = defaultdict(dict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited
                    )
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results


if __name__ == "__main__":
    solution = Solution()
    inputs = [
        [
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        ],
        [
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        ],
        [[["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]],
        [
            [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
            [3.0, 4.0, 5.0, 6.0],
            [
                ["x1", "x5"],
                ["x5", "x2"],
                ["x2", "x4"],
                ["x2", "x2"],
                ["x2", "x9"],
                ["x9", "x9"],
            ],
        ],
        [
            [["a", "b"], ["c", "d"]],
            [1.0, 1.0],
            [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
        ],
    ]
    expected = [
        [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        [3.75000, 0.40000, 5.00000, 0.20000],
        [0.50000, 2.00000, -1.00000, -1.00000],
        [360.0, 0.008333333333333333, 20, 1, -1, -1],
        [-1, -1, 1, 1],
    ]

    funcs = [solution.calcEquation, solution.calcEquation_2]
    for f, input, expect in (
        (f, i, e) for i, e in zip(inputs, expected) for f in funcs
    ):
        print(f"\nRunning {f.__name__}")
        for input, expect in zip(inputs, expected):
            output = f(*input)
            assert output == expect, f"{input=}, {expect=}, {output=}"
            t = timeit(
                stmt=f"f({input[0]}, {input[1]}, {input[2]})",
                number=10_000,
                globals=globals(),
            )
            print(f"{f.__name__} took: {t:.6f}")

    print("PASSED!!!")
