def test_case(input):
    expected = 6
    actual = main(input)
    assert expected == actual

def main(input):
    n, m = [int(val) for val in input.split(" ")]

    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = sum(dp[i-1][1:])
            else:
                dp[i][j] = dp[i-1][j-1]
    return sum(dp[-1][:])

if __name__ == "__main__":
    test_case("6 4")
    input = open("rosalind_fibd.txt", 'r').read()
    print(main(input))
