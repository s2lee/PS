def pooling(matrix):
    matrix_size = len(matrix)
    if matrix_size == 1:
        return matrix[0][0]

    new_matrix = [[] for _ in range(matrix_size//2)]
    for i in range(0, matrix_size, 2):
        for j in range(0, matrix_size, 2):
            new_matrix[i//2].append(sorted([matrix[i][j],
                                            matrix[i][j+1],
                                            matrix[i+1][j],
                                            matrix[i+1][j+1]])[2])
    return pooling(new_matrix)


N = int(input())
initial_matrix = [list(map(int, input().split())) for _ in range(N)]
print(pooling(initial_matrix))
