def test_case(input):
    expected = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323"""
    actual = main(input)
    assert expected == actual

def main(input):
    split_input = input.split("\n")
    dna_map = {}

    current_dna = ""
    current_name = ""
    for idx, val in enumerate(split_input):
        if "Rosalind" in val:
            if idx != 0:
                dna_map[current_name] = current_dna
                current_dna = ""
                current_name = val.lstrip(">")
            else:
                current_name = val.lstrip(">")
        else:
            current_dna += val

    dna_map[current_name] = current_dna
    graph = {}

    for dna_name in dna_map:
        graph[dna_name] = []
        suffix = dna_map[dna_name][-3:]
        for other_dna_name in dna_map:
            if other_dna_name != dna_name:
                prefix = dna_map[other_dna_name][:3]
                if suffix == prefix:
                    graph[dna_name].append(other_dna_name)

    result = ""
    for node in graph:
        for neigbour in graph[node]:
            result += f"{node} {neigbour}\n"

    return result.rstrip("\n")

if __name__ == "__main__":
    test_case(""">Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG""")
    input = open("rosalind_grph.txt", 'r').read()
    print(main(input))
