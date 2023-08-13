from math import comb

def test_case(input):
    expected = 0.684
    actual = main(input)
    assert expected == actual

def main(input):
    k, N = [int(val) for val in input.split(" ")]
    P = 2**k
    probability = 0
    for i in range(N, P + 1):
        probability += comb(P, i) * 0.25**i * 0.75**(P-i)
    return float('{:0.3f}'.format(probability))

if __name__ == "__main__":
    test_case("2 1")
    input = open("rosalind_lia.txt", 'r').read()
    print(main(input))
