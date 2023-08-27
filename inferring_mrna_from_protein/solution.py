import requests
from Bio import SeqIO
from io import StringIO
import re


def test_case(input):
    expected = 12
    actual = main(input)
    assert expected == actual

def main(input):

    lookup_table = {
        "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
        "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
        "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
        "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
        "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
        "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
        "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
        "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
        "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
        "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
        "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
        "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
        "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
        "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
        "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
        "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
    }

    frequency_map = {}
    for i in lookup_table:
        val = lookup_table[i]
        if val not in frequency_map:
            frequency_map[val] = 0
        frequency_map[val] += 1

    permutations = 1
    for i in input:
        permutations *= frequency_map[i]
        permutations %= 1_000_000

    permutations *= frequency_map["Stop"]
    return permutations % 1_000_000


if __name__ == "__main__":
    test_case("MA")
    input = open("rosalind_mrna.txt", 'r').read()
    print(main(input))
