def is_balanced(s: str) -> bool:
    pairs = {"{": "}", "[": "]", "(": ")"}
    stock = []

    for br in s:
        if br in pairs:
            stock.append(br)
        elif not stock or pairs[stock.pop()] != br:
            return False
    return not stock


if __name__ == "__main__":
    inputs = [
        ["{[()]}", True],
        ["{}()", True],
        ["{(})", False],
        ["{[(])}", False],
        ["{{[[(())]]}}", True],
    ]

    for input, expected in inputs:
        output = is_balanced(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
