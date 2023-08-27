from Bio import SeqIO
import re
from Bio.Seq import Seq

def test_case(input):
    expected = set({"MLLGSFRLIPKETLIQVAGSSPCNLS", "M", "MGMTPRLGLESLLE", "MTPRLGLESLLE"})
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

    reverse_complement_dna = get_reverse_complement_dna(dna)

    def get_protein(dna):
        look_up_table = {
            'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
            'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
            'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
            'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
            'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
            'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
            'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
            'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
            'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
            'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
            'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
            'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
            'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
            'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
            'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
            'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
        }

        start_codon = "ATG"
        pos_iter = re.finditer(pattern=start_codon, string=dna)
        start_pos = []
        for i in pos_iter:
            start_pos.append(i.span()[0])

        current_idx = start_pos[0]
        protein_count = 0
        result_proteins = set()
        for pos in start_pos:
            found_stop_codon = False
            current_idx = pos
            protein = ""

            while not found_stop_codon:
                if current_idx + 3 > len(dna):
                    break
                codon = dna[current_idx: current_idx + 3]
                if codon in look_up_table and look_up_table[codon] != 'Stop':
                    current_idx += 3
                    protein += look_up_table[codon]
                else:
                    found_stop_codon = True
                    result_proteins.add(protein)
        return result_proteins

    results = get_protein(dna)
    reverse_results = get_protein(reverse_complement_dna)

    total = results.union(reverse_results)
    print("\n".join(list(total)))
    return total



if __name__ == "__main__":
    test_case("test.txt")
    print("--Solution--")
    main("rosalind_orf.txt")
