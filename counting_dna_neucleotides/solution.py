from collections import Counter

def test_case(input):
    expected = "20 12 17 21"
    actual = main(input)
    assert expected == actual


def main(dna_string):
    freq_map = Counter(dna_string)

    # Neucleobases list
    neucleobases = ['A', 'C', 'G', 'T']
    result = []
    for neucleobase in neucleobases:
        result.append(str(freq_map[neucleobase]))
    return " ".join(result)

if __name__ == "__main__":
    test_case("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
    input = open("rosalind_dna.txt", 'r').read()
    print(main(input))
