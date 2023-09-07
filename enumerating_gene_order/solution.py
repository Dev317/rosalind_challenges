from itertools import permutations

def test_case(input):
    expected_num_permutations = 6
    expected_permutations = set({
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1)
    })
    num_permutations, permutations = main(input)
    assert expected_num_permutations == num_permutations
    assert expected_permutations == permutations

def main(input):
    num = int(input)
    p = list(permutations(list(range(1, num+1))))
    per_set = set()
    for per in p:
        per_set.add(per)
    return len(p), per_set


if __name__ == "__main__":
    test_case("3")
    input = open("rosalind_perm.txt", 'r').read()
    num_permutations, per = main(input)
    print(num_permutations)

    for p in per:
        for i in p:
            print(i, end=" ")
        print()
