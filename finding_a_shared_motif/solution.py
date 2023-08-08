from Bio import SeqIO

def test_case(input):
    expected = "AC"
    actual = main(input)
    assert expected in actual

def main(input):
    dnas = []
    with open(input) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            dnas.append(str(record.seq))

    dnas = sorted(dnas, key=len)
    base_seq = dnas[0]
    other_seq = dnas[1:]

    motifs = []
    bl = False
    for i in range(len(base_seq)):
        for j in range(i, len(base_seq)):
            motif = base_seq[i:j+1]
            for seq in other_seq:
                if motif in seq:
                    bl = True
                else:
                    bl = False
                    break
            if len(motif) > 1 and bl == True:
                motifs.append(motif)

    sorted_motifs = sorted(motifs, key=len, reverse=True)
    return sorted_motifs

if __name__ == "__main__":
    test_case("test.txt")
    input = "rosalind_lcsm.txt"
    print(main(input)[0])
