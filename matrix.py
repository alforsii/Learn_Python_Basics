
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# How we can print each elem in the matrix ?
# 1. Shorter version
for row in matrix:
    for col in row:
        print(col)

# 2. Longer version
row_length = len(matrix)
for i in range(row_length):
    col_length = len(matrix[i])
    for j in range(col_length):
        print(matrix[i][j])
