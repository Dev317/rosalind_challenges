def test_case(input):
    expected = 19
    actual = main(input)
    assert expected == actual


def main(input):
    n = int(input.split(" ")[0])
    k = int(input.split(" ")[1])

    if n == 1:
        return 1

    if n == 2:
        return 1

    arr = [0] * n
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]*k

    return arr[-1]

if __name__ == "__main__":
    test_case("5 3")

    input = open("rosalind_fib.txt", 'r').read()
    print(main(input))
