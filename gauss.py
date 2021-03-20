import math
import os


# læser fil man har givet
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



# input section
theinput = splitted2 # hver liste inde i listen er en række i en matrix.

# danner enhedsmatrix
enhedsMatrix = []
for i in range(len(theinput)):
    enhedsMatrix.append([])
    # tilføj 0'er og 1'ere til enhedsmatricen
    for j in range(len(theinput)):
        if j==i:
            enhedsMatrix[i].append(1)
        else:
            enhedsMatrix[i].append(0)
enhedsMatrixNy = enhedsMatrix



def operation(x, y, row, matrix, matrix1, const): # x og y er kordinaterne for det punkt der skal laves om. row er den række som man tager udgangspunkt i. matrix er den matrix der skal bruges. y starter oppefra
    out = matrix1[y][x] - ((matrix1[row][x])/(matrix[row][row]) * const)
    return out

# doing the things
for row in range(len(theinput)): # for hver række som er udgangspunkt
    for y in range(len(theinput)):
        if y != row:
            const = theinput[y][row]
            const2 = enhedsMatrixNy[y][row]
            for x in range(len(theinput) + 1):
                theinput[y][x] = operation(x, y, row, theinput, theinput, const)
                if x != (len(theinput)):
                    enhedsMatrixNy[y][x] = operation(x, y, row, theinput, enhedsMatrixNy, const)
                

# printing the things
for i in range(len(theinput)):
    print(f'value #{i} is: {theinput[i][len(theinput)]/theinput[i][i]}')

for i in range(len(enhedsMatrixNy)):
    for j in range(len(enhedsMatrixNy)):
        enhedsMatrixNy[i][j] /= theinput[i][i]
print("Invers matrix", enhedsMatrixNy)
