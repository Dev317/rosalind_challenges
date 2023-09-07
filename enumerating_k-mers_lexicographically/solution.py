from itertools import permutations, combinations

def test_case(input):
    expected = """AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
"""
    actual = main(input)
    assert expected == actual

def main(input):
    input = input.split("\n")
    symbols = input[0].split(" ")
    length = int(input[1])
    result = ""

    for _ in range(length - 1):
        symbols.extend(symbols)

    p = list(combinations(list(symbols), r=length))

    p_set = set()

    for per in p:
        p_set.add(tuple(per))

    result = ""
    sorted_per = sorted(list(p_set))
    for per in sorted_per:
        result += "".join(per) + "\n"

    return result

if __name__ == "__main__":
    test_case("""A C G T
2""")
    input = open("rosalind_lexf.txt", 'r').read()
    print(main(input))
