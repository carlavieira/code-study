def set_zeros(matrix):

    rows = [False]*len(matrix)
    columns = [False]*len(matrix[0])

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 0:
                rows[i] = True
                columns[j] = True

    for row_index, have_zero in enumerate(rows):
        if have_zero:
            matrix[row_index] = [0]*len(matrix[0])

    for column_index, have_zero in enumerate(columns):
        if have_zero:
            for row_index in range(len(matrix)):
                matrix[row_index][column_index] = 0


matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
set_zeros(matrix)
print(matrix)