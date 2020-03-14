'''
Matrix multiplier - by Renato Bittencourt
'''

# open files to get matrix
matrix1File = open("./matrix/matrix1.txt", "r")
matrix2File = open("./matrix/matrix2.txt", "r")

# save file content on Strings
matrix1String = matrix1File.read()
matrix2String = matrix2File.read()

# split strings to get row
matrix1Rows = matrix1String.split("\n")
matrix2Rows = matrix2String.split("\n")

# save rows number of matrix
r1 = len(matrix1Rows)
r2 = len(matrix2Rows)

# set the row numbers to matrix
matrix1 = [0]*r1
matrix2 = [0]*r2

# split each row to get elements
for r in range(r1):
    matrix1[r] = matrix1Rows[r].split(" ")
for r in range(r2):
    matrix2[r] = matrix2Rows[r].split(" ")

# save column number of matrix
c1 = len(matrix1[0])
c2 = len(matrix1[2])

# validate matrix indexes

if c1 != r2:
    # matrix don't matches
    print("ERRO: O número de colunas da matriz 1 deve ser igual ao número de linhas da matriz 2.")
else:
    # matrix matches
    matrixResult = [0] * r1
    for r in range(r1):
        matrixResult[r] = [0] * c2

    # assign product in matrix result
    for r3 in range(r1):
        for c3 in range(c2):
            matrixResult[r3][c3] = 0
            for i in range(r2):
                matrixResult[r3][c3] += int(matrix1[r3][i]) * int(matrix2[i][c3])

    # save new matrix on file
    result = open("./matrix/RESULT.txt", "w+")
    for j in range(0, len(matrixResult)):
        for i in range(0, len(matrixResult[0])):
            result.write("%d\t" % (matrixResult[j][i]))
        result.write("\n")
    print(matrixResult)



