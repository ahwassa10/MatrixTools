#matrixTools.py
#Sunday, September 27, 2020
import staticMatrix

def buildMatrix(inputString, formattingFunction):
    data = []
    iterator = 0
    tempRow = []
    
    while iterator < len(inputString):
        character = inputString[iterator]
        if character.isspace() or character == ",":
            iterator = iterator + 1
            continue 
        elif character == ";":
            if len(tempRow) != 0:
                data.append(tempRow)
            iterator = iterator + 1
            tempRow = []
            continue
        else:
            word = ""
            while character.isnumeric() or character == "." or character == "-":
                word = word + character
                iterator = iterator + 1
                if iterator < len(inputString):
                    character = inputString[iterator]
                else:
                    break
            tempRow.append(formattingFunction(word))
    if len(tempRow) != 0:
        data.append(tempRow)
    
    rows = len(data)
    if rows == 0:
        raise staticMatrix.invalidMatrixDimensionsError
    columns = len(data[0])
    
    returnMatrix = staticMatrix.staticMatrix(rows, columns)
    returnMatrix.setData(data)
    return returnMatrix

def add(matrix1, matrix2):
    if matrix1.rows != matrix2.rows:
        raise staticMatrix.invalidMatrixDimensionsError
    else:
        rows = matrix1.rows
    
    if matrix1.columns != matrix2.columns2:
        raise staticMatrix.invalidMatrixDimensionsError
    else:
        columns = matrix1.columns
    
    data = []
    for i in range(rows):
        tempRow = []
        for j in range(columns):
            entry = matrix1.data[i][j] + matrix2.data[i][j]
            tempRow.append(entry)
        data.append(tempRow)
    
    returnMatrix = staticMatrix.staticMatrix(rows, columns)
    returnMatrix.setData(data)
    return returnMatrix

def scalarMultiply(matrix, scalar):
    data = []
    for i in range(matrix.rows):
        tempRow = []
        for j in range(matrix1.columns):
            entry = matrix.data[i][j] * scalar
            tempRow.append(entry)
        data.append(tempRow)
    
    returnMatrix = staticMatrix.staticMatrix(matrix.rows, matrix.columns)
    returnMatrix.setData(data)
    return returnMatrix
        