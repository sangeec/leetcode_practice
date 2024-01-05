def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n // 2):
        first = i
        last = n - 1 - i

        for j in range(first, last):
            offset = j - first

            # Save top
            top = matrix[first][j]

            # Move left to top
            matrix[first][j] = matrix[last - offset][first]

            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move right to bottom
            matrix[last][last - offset] = matrix[j][last]

            # Move top to right
            matrix[j][last] = top


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

rotate_matrix(matrix)

print("\nRotated Matrix:")
for row in matrix:
    print(row)
