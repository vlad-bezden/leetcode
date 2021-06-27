def matching_pairs(s, t):
    # same string, must swap anyway
    if s == t:
        return len(s) - 2

    cand_s = {}
    cand_t = {}
    counter = 0
    found = False
    for i, (sc, tc) in enumerate(zip(s, t)):
        if sc == tc:
            counter += 1
        elif not found:
            # different chars in two strings check if we can swap
            # and get match
            if cand_t.get(sc, set()) & cand_s.get(tc, set()):
                # we found match and we can swap
                found = True
                counter += 2
            else:
                # no swap found, add chars to the candidate list
                cand_s.setdefault(sc, set()).add(i)
                cand_t.setdefault(tc, set()).add(i)

    if not found:
        # not found swap, we still need to perform swap
        # check if we have at list one common chars in two str
        # then we can swap something and get extra one char
        if set(cand_s.keys()) & set(cand_t.keys()):
            counter += 1
        # there are no common chars for swapping, but we still
        # need to perform swapping, which will decremate found counter
        elif counter > 0:
            counter -= 1

    return counter


if __name__ == "__main__":
    inputs = [
        (["axb", "ayb"], 1),
        (["mno", "mno"], 1),
        (["abcd", "adcb"], 4),
        (["abcde", "adcbe"], 5),
        (["abced", "bedca"], 1),
        (["abcd", "abcd"], 2),
        (["abjcdx", "zyxtnj"], 2),
        (["ab", "ba"], 2),
        (["ab", "ab"], 0),
        (["ab", "cd"], 0),
        (["ax", "ya"], 1),
    ]

    for input, expected in inputs:
        result = matching_pairs(*input)
        assert result == expected, f"{input=}, {expected=}, {result=}"

    print("PASSED!!!")
