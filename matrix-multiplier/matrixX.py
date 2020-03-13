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

# set the row numbers to matrix
matrix1 = [0]*len(matrix1Rows)
matrix2 = [0]*len(matrix2Rows)

# split each row to get elements
for r in range(len(matrix1Rows)):
    matrix1[r] = matrix1Rows[r].split(" ")
for r in range(len(matrix2Rows)):
    matrix2[r] = matrix2Rows[r].split(" ")

print(matrix1)



