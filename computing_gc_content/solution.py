from collections import Counter

def test_case(input):
    expected_name, expected_value = "Rosalind_0808", 60.919540
    actual_name, actual_value = main(input)
    assert expected_name == actual_name
    assert 0.001 > abs(expected_value - actual_value)


def main(input):

    def get_dna_map(input):
        input_split = input.split("\n")
        dna_names = []
        dna_strings = []
        current_dna_string = ""

        for idx, value in enumerate(input_split):
            if "Rosalind" in value:
                dna_names.append(value.replace(">",""))
                if idx != 0:
                    dna_strings.append(current_dna_string)
                    current_dna_string = ""
            else:
                current_dna_string += value
        dna_strings.append(current_dna_string)
        dna_map = dict(zip(dna_names, dna_strings))
        return dna_map

    def get_gc_content(dna_string):
        freq_map = Counter(dna_string)
        gc_content = (freq_map['C'] + freq_map['G']) / len(dna_string) * 100

        return float("{:.6f}".format(gc_content))

    dnas = get_dna_map(input)
    highest_gc_content = 0
    highest_gc_content_dna_name = ""

    for dna in dnas:
        dna_gc_content = get_gc_content(dnas[dna])
        if dna_gc_content > highest_gc_content:
            highest_gc_content = dna_gc_content
            highest_gc_content_dna_name = dna
    return highest_gc_content_dna_name, highest_gc_content

if __name__ == "__main__":
    test_case(""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT""")

    input = open("rosalind_gc.txt", 'r').read()
    print(main(input))
