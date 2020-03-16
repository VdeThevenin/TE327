'''
Matrix multiplier - by Renato Bittencourt
GRR20182103
'''

import datetime
import os


currentDT = datetime.datetime.now()
curDT = str(currentDT).replace("-", "_").replace(" ", "_").replace(":", "-").split(".")[0]

folder = "result_" + curDT
os.mkdir("./matrix/" + folder)


def createIdentityMatrix(n):
    identity = [0] * int(n)
    for u in range(0, int(n)):
        identity[u] = [0] * int(n)
        identity[u][u] = 1
    return identity


def saveMatrix(matrix, name):
    result = open("./matrix/" + folder + "/" + name + ".txt", "w+")
    for j in range(0, len(matrix)):
        for k in range(0, len(matrix[0])):
            if k < len(matrix[0]) - 1:
                result.write("%d\t" % int(matrix[j][k]))
            else:
                result.write("%d" % int(matrix[j][k]))
        if j < len(matrix) - 1:
            result.write("\n")
    print(matrix)


# open files to get matrix
matrix1File = open("./matrix/matrix1.txt", "r")
matrix2File = open("./matrix/matrix2.txt", "r")

# save file content on Strings
matrix1String = matrix1File.read()
matrix2String = matrix2File.read()

# split strings to get row
matrix1Rows = matrix1String.split("\n")
matrix2Rows = matrix2String.split("\n")

# print(matrix1String, matrix2String)
# save rows number of matrix
r1 = len(matrix1Rows)
r2 = len(matrix2Rows)

# set the row numbers to matrix
matrix1 = [0]*r1
matrix2 = [0]*r2

# split each row to get elements
for r in range(r1):
    matrix1[r] = matrix1Rows[r].split("\t")
for r in range(r2):
    matrix2[r] = matrix2Rows[r].split("\t")

# save column number of matrix
c1 = len(matrix1[0])
c2 = len(matrix2[0])

# verify its not about identity matrix definition
if r1 == 1 and c1 == 1:
    r1 = int(matrix1[0][0])
    c1 = int(matrix1[0][0])
    matrix1 = createIdentityMatrix(matrix1[0][0])
saveMatrix(matrix1, "matrix1")
if r2 == 1 and c2 == 1:
    r2 = int(matrix2[0][0])
    c2 = int(matrix2[0][0])
    matrix2 = createIdentityMatrix(matrix2[0][0])
saveMatrix(matrix2, "matrix2")

# validate matrix indexes
if c1 != r2:
    print(c1, " != ", r2)
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
    saveMatrix(matrixResult, "RESULT")

