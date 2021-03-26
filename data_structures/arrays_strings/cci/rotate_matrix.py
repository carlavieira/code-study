def rotate_matrix(matrix):
    if not matrix or len(matrix) != len(matrix[0]): raise Exception("Invalid matrix")
    n = len(matrix)
    for layer in range(n// 2):
        # coordenates of the layer squa
        first = layer
        last = n - 1 - layer

        swap_layer(matrix, first, last)


def swap_layer(matrix, first, last):
    for i in range(first, last):
        aux = matrix[first][i]

        # top receives left
        matrix[first][i] = matrix[last-i][first]

        # left receives bottom
        matrix[last-i][first] = matrix[last][last-i]

        #bottom receives right
        matrix[last][last-i] = matrix[i][last]

        #right recieves top
        matrix[i][last] = aux


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print("------")

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 20, 11, 12], [13, 14, 15, 16]]
print_matrix(matrix)
rotate_matrix(matrix)
print_matrix(matrix)
