A = [
    [1, 2],
    [3, 4],
    [5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]


def main():
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    res = [[0 for k in range(cols_B)] for i in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                res[i][j] += A[i][k] * B[k][j]

                res[0][0] = 1*7+2*10
                res[0][1] = 1*8 + 2*11
    for i in res:
        print(i)

if __name__ == '__main__':
    main()