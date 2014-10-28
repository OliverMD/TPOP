# A matrix will be represented as a list of lists of floats.
# Each list of floats will represent a row. So matrix[0][1]
# would be row 0, column 1.

def print_matrix(matrix):
    # print_matrix(matrix [[float]]) -> None
    # Prints the matrix in a readable form to the standard
    # output

    for row in matrix:
        for elm in row:
            print elm,
            print " "*(5 - len(str(elm))),
        print "\n"
    return

def scalar_product(scalar, matrix):
    # scalar_product(scalar float, matrix [[float]]) -> None
    # Calculates scalar product and prints the matrix
    
    matrix  = [[elm * scalar for elm in row] for row in matrix]
    print_matrix(matrix)
    return

def add_matrix(matrix1, matrix2):
    # add_matrix(matrix1 [[float]], matrix2 [[float]]) -> None
    # Function adds each element of the matrices together
    # and prints the resulting matrix.
    
    if len(matrix1) != len(matrix2):
        print "matrices aren't of same dimension!"
        return
    newmat = []
    for row in range(len(matrix1)):
        if len(matrix1[row]) != len(matrix2[row]):
            print "matrices aren't of same dimension!"
            return
        newmat.append([])
        for col in range(len(matrix1[row])):
            newmat[row].append(matrix1[row][col] + matrix2[row][col])
    print_matrix(newmat)
    return
    
def transpose_matrix(matrix):#
    # transpose_matrix(matrix [[float]]) -> None
    # Transposes the matrix and prints the
    # resulting matrix.
    
    newmat = []
    for j in range(len(matrix[0])):
        newmat.append([])
        for i in range(len(matrix)):
            newmat[j].append(matrix[i][j])
    print_matrix(newmat)
    return

def wise_man():
    # wise_man() -> None
    # Solves the king and wise
    # man chess problem.
    weight = 0
    for i in range(8):
        for j in range(8):
            weight += (2 ** (j+(i*8))) * 30
            print str((2 ** (j+(i*8)))*30)+"mg",
        print ""
    print str(weight)+"mg"
    
