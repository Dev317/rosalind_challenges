def test_case(input):
    expected = "GAUGGAACUUGACUACGUAAAUU"
    actual = main(input)
    assert expected == actual

def main(input):
    result = ""
    for i in range(len(input)):
        if input[i] == "T":
            result += "U"
        else:
            result += input[i]
    return result

if __name__ == "__main__":
    test_case("GATGGAACTTGACTACGTAAATT")
    input = open("rosalind_rna.txt", 'r').read()
    print(main(input))
