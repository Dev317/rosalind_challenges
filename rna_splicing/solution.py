from Bio import SeqIO
import re
from Bio.Seq import Seq

def test_case(input):
    expected = "MVYIADKQHVASREAYGHMFKVCA"
    actual = main(input)
    assert expected == actual

def main(input):
    seq = []
    with open(input) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            seq.append(str(record.seq))

    result = seq[0]
    introns = seq[1:]


    for intron in introns:
        result = result.replace(intron, "")

    result = Seq(result)
    result = result.translate(to_stop=True)
    return str(result)

if __name__ == "__main__":
    test_case("test.txt")
    solution = main("rosalind_splc.txt")
    print(solution)
