def test_case(input):
    expected = "ACCGGGTTTT"
    actual = main(input)
    assert expected == actual


def main(input):
    complement_map = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    reverse = input[::-1]
    result = ""

    for i in reverse:
        result += complement_map[i]

    return result

if __name__ == "__main__":
    test_case("AAAACCCGGT")

    input = open("rosalind_revc.txt", 'r').read()
    print(main(input))
