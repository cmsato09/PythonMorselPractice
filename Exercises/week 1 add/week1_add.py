
def add(matrix1, matrix2):
    """ Add a 2x2 matrix together. matrix represented by a a list-of-lists"""
    results = []
    for rows in zip(matrix1, matrix2):
        temp_row = []
        for items in zip(rows[0], rows[1]):
            temp_row.append(items[0] + items[1])
        results.append(temp_row)
    return results


def add_mult(*matrix):
    # create list of all matrix
    results = []
    for row in zip(*matrix):
        temp_row = []
        for values in zip(*row):
            temp_row.append(sum(values))

        results.append(temp_row)

    return results


if __name__ == "__main__":
    matrixA = [[1, -2], [-3, 4]]
    matrixB = [[2, -1], [0, -1]]

    matrixC = [[1,0,0],[0,1,0],[0,0,1]]
    matrixD = [[1,1,3],[0,0,3],[5,4,7]]
    matrixE = [[1,1,3],[0,0,3],[5,4,7]]
    #print(add(matrixA, matrixB))
    print(add_mult(matrixC, matrixC, matrixC, matrixC))
