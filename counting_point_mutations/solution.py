def test_case(input):
    expected = 7
    actual = main(input)
    assert expected == actual


def main(input):
    dna_string_1, dna_string_2 = input.split("\n")
    counter = 0
    for i in range(len(dna_string_1)):
        if dna_string_1[i] != dna_string_2[i]:
            counter += 1
    return counter

if __name__ == "__main__":
    test_case("""GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT""")

    input = open("rosalind_hamm.txt", 'r').read()
    print(main(input))
