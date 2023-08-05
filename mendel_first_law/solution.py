from math import comb

def test_case(input):
    expected = 0.78333
    actual = main(input)
    assert expected == actual


def main(input):

    k, m, n = [int(val) for val in input.split(" ")]

    # homo d, homo d : 1
    # homo d, hetero : 1
    # homo d, homo r: 1
    # hetro, hetro: 0.75
    # hetro, homo r: 0.5

    total_comb = comb(k+m+n, 2)
    valid_comb = 1 * comb(k,2) + 1*k*m + 1*k*n + 0.75*comb(m,2) + 0.5*m*n
    prob = valid_comb / total_comb

    return float("{:.5f}".format(prob))

if __name__ == "__main__":
    test_case("""2 2 2""")

    input = open("rosalind_iprb.txt", 'r').read()
    print(main(input))
