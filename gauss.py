import math
import os

myFile = open('pythontext.txt')
read = myFile.read()
splitted1 = read.split('\n')
del splitted1[-1]
splitted2 = []
for i in range(len(splitted1)):
    rowA = splitted1[i].split(',')
    splitted2.append(rowA)
    for j in range(len(splitted2[i])):
        splitted2[i][j] = int(splitted2[i][j])


print("FILEN: \n", splitted2)

# input section
theinput = splitted2 # hver liste inde i listen er en række i en matrix.

def operation(x, y, row, matrix, const): # x og y er kordinaterne for det punkt der skal laves om. row er den række som man tager udgangspunkt i. matrix er den matrix der skal bruges. y starter oppefra
    out = matrix[y][x] - ((matrix[row][x])/(matrix[row][row]) * const)
#    print("XY=", x, y, "row:", row, "was:", matrix[y][x], "is:", out)
#    print(matrix)
    return out

# doing the things
for row in range(len(theinput)): # for hver række som er udgangspunkt
    for y in range(len(theinput)):
        if y != row:
            const = theinput[y][row]
            for x in range(len(theinput) + 1):
                theinput[y][x] = operation(x, y, row, theinput, const)
                

# printing the things
for i in range(len(theinput)):
    print(f'value #{i} is: {theinput[i][len(theinput)]/theinput[i][i]}')
