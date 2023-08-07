def test_case(input):
    expected = 3.5
    actual = main(input)
    assert expected == actual

def main(input):
    input_split = [int(val) for val in input.split(" ")]
    prob = [1, 1, 1, 0.75, 0.5, 0]
    return sum(2 * input_split[i] * prob[i] for i in range(len(prob)))

if __name__ == "__main__":
    test_case("1 0 0 1 0 1")
    input = open("rosalind_iev.txt", 'r').read()
    print(main(input))
