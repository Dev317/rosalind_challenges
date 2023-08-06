def test_case(input):
    expected = """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""
    actual = main(input)
    assert expected == actual

def main(input):
    split_input = input.split("\n")

    dna_strings = []
    current_dna = ""
    for idx, val in enumerate(split_input):
        if "Rosalind" not in val:
            current_dna += val
        elif idx != 0:
            dna_strings.append(current_dna)
            current_dna = ""

    dna_strings.append(current_dna)

    profile_map = {
        "A": [0] * len(dna_strings[0]),
        "C": [0] * len(dna_strings[0]),
        "G": [0] * len(dna_strings[0]),
        "T": [0] * len(dna_strings[0]),
    }

    for dna in dna_strings:
        for idx in range(len(dna)):
            profile_map[dna[idx]][idx] += 1

    result = ""
    consensus = ""
    for idx in range(len(dna_strings[0])):
        max_val = 0
        consensus_base = ""
        for neucleobase in profile_map:
            if profile_map[neucleobase][idx] > max_val:
                max_val = profile_map[neucleobase][idx]
                consensus_base = neucleobase
        consensus += consensus_base

    result += consensus + "\n"
    for consensus_base in profile_map:
        result += consensus_base + ": " + " ".join([str(val) for val in profile_map[consensus_base]]) + "\n"

    return result.rstrip("\n")



if __name__ == "__main__":
    test_case(""">Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT""")
    input = open("rosalind_cons.txt", 'r').read()
    print(main(input))
