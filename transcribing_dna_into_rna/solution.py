def test_case(input):
    expected = "GAUGGAACUUGACUACGUAAAUU"
    actual = main(input)
    assert expected == actual


def main(dna_string):
    result = ""
    for i in range(len(dna_string)):
        if dna_string[i] == "T":
            result += "U"
        else:
            result += dna_string[i]
    print(result)

if __name__ == "__main__":
    test_case("GATGGAACTTGACTACGTAAATT")
    dna_string = open("rosalind_rna.txt", 'r').read()
    main(dna_string)
