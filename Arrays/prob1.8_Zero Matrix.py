# def zero_matrix(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#     zero_rows, zero_cols = set(), set()

#
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 zero_rows.add(i)
#                 zero_cols.add(j)

#
#     for row in zero_rows:
#         for j in range(cols):
#             matrix[row][j] = 0

#
#     for col in zero_cols:
#         for i in range(rows):
#             matrix[i][col] = 0

#
# matrix = [
#     [1, 2, 3],
#     [4, 0, 6],
#     [7, 8, 9]
# ]

# print("Original Matrix:")
# for row in matrix:
#     print(row)

# zero_matrix(matrix)

# print("\nMatrix after Zero Transformation:")
# for row in matrix:
#     print(row)


def set_zeros(matrix):
    row_has_zero = False
    col_has_zero = False

    for j in range(len(matrix[0])):
        print("matrix 0")
        print(matrix[0])
        if matrix[0][j] == 0:
            row_has_zero = True
            break

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_has_zero = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)

    if row_has_zero:
        nullify_row(matrix, 0)

    if col_has_zero:
        nullify_column(matrix, 0)


def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_column(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

set_zeros(matrix)

print("\nMatrix after Zero Transformation:")
for row in matrix:
    print(row)
