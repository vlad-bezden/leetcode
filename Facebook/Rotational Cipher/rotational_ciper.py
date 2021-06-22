from string import ascii_lowercase, ascii_uppercase, digits


def rotationalCipher(input, rotation_factor):
    ascii = "".join(l + u for l, u in zip(ascii_lowercase, ascii_uppercase))
    result = []
    for c in input:
        if (i := ascii.find(c)) >= 0:
            c = ascii[(i + rotation_factor * 2) % 52]
        elif (i := digits.find(c)) >= 0:
            c = digits[(i + rotation_factor) % 10]
        result.append(c)
    return "".join(result)


if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    assert expected_1 == output_1

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    assert expected_2 == output_2

    print("PASSED!!!")
