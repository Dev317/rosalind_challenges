import requests
from Bio import SeqIO
from io import StringIO
import re


def test_case(input):
    expected = """B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614"""
    actual = main(input)
    assert expected == actual

def main(input):
    input_split = input.split("\n")
    proteins = [protein.split("_")[0] for protein in input_split]

    def get_dna(protein):
        url = f"https://rest.uniprot.org/uniprotkb/{protein}.fasta"
        response = requests.get(url)
        records = SeqIO.parse(StringIO(response.text), "fasta")
        return str(next(records).seq)

    def find_motifs_pos(dna):
        pattern = "(?=(N[^P][S|T][^P]))"
        pos_iter = re.finditer(pattern=pattern, string=dna)
        pos = []
        for i in pos_iter:
            pos.append(str(i.span()[0] + 1))
        return pos

    result = ""

    for idx, protein in enumerate(proteins):
        dna = get_dna(protein)
        pos = find_motifs_pos(dna)

        if len(pos):
            result += input_split[idx] + "\n"
            result += " ".join(pos) + "\n"
    return result.rstrip("\n")

if __name__ == "__main__":
    test_case("""A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST""")
    input = open("rosalind_mprt.txt", 'r').read()
    print(main(input))
