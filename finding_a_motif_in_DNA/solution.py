def test_case(input):
    expected = "2 4 10"
    actual = main(input)
    assert expected == actual

def main(input):
    dna_string, substring = input.split("\n")
    indices = [index + 1 for index in range(len(dna_string)) if dna_string.startswith(substring, index)]
    return " ".join([str(idx) for idx in indices])

if __name__ == "__main__":
    test_case("""GATATATGCATATACTT
ATAT""")
    input = open("rosalind_subs.txt", 'r').read()
    print(main(input))
