def solve(matrix, r):

    # no. of layers
    k = min(m,n) // 2
    mat = []

    for i in range(k):

        temp = []
        for j in range(i, n-i-1):
            temp.append(matrix[i][j])
        for j in range(i, m-i-1):
            temp.append(matrix[j][n-i-1])
        for j in range(n-1-i, i, -1):
            temp.append(matrix[m-i-1][j])
        for j in range(m-1-i, i, -1):
            temp.append(matrix[j][i])

        mat.append(temp)

    for i in range(k):
        row = mat[i]
        idx = r % len(row)
        if i % 2 == 0:
            def inc():
                return (idx + 1) % len(row)

            for j in range(i, n-i-1):
                matrix[i][j] = row[idx]
                idx = inc()
            for j in range(i, m-i-1):
                matrix[j][n-i-1] = row[idx]
                idx = inc()
            for j in range(n-1-i, i, -1):
                matrix[m-i-1][j] = row[idx]
                idx = inc()
            for j in range(m-1-i, i, -1):
                matrix[j][i] = row[idx]
                idx = inc()
        else:
            temp1 = row[:len(row)-r]
            temp2 = row[len(row)-r:]
            temp2.extend(temp1)
            def inc():
                return (idx+1) % len(row)

            for j in range(i, n-i-1):
                matrix[i][j] = temp2[idx-1]
                idx = inc()
            for j in range(i, m-i-1):
                matrix[j][n-i-1] = temp2[idx-1]
                idx = inc()
            for j in range(n-1-i, i, -1):
                matrix[m-i-1][j] = temp2[idx-1]
                idx = inc()
            for j in range(m-1-i, i, -1):
                matrix[j][i] = temp2[idx-1]
                idx = inc()

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    solve(matrix, r)


for row in matrix:
    print(*row)