from Bio import SeqIO
import re
from Bio.Seq import Seq

def test_case(input):
    expected = """4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""
    actual = main(input)
    assert expected == actual

def main(input):
    dna = None
    with open(input) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            dna = str(record.seq)
            break

    def get_reverse_complement_dna(dna):
        lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        return ''.join([lookup[c] for c in reversed(dna)])

    def is_reverse_palindrome(dna):
        return dna == get_reverse_complement_dna(dna)

    result = ""

    for i in range(len(dna)):
        for j in range(4, 13):
            if i + j <= len(dna):
                test_dna_string = dna[i:i+j]
                if is_reverse_palindrome(test_dna_string):
                    result += f"{i + 1} {j}\n"

    return result

if __name__ == "__main__":
    test_case("test.txt")
    solution = main("rosalind_revp.txt")
    print(solution)
