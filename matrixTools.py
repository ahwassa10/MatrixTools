def toMatrix(string):
    m = []
    
    row = []
    
    charPointer = 0
    longest = 0
    
    while charPointer < len(string):
        if string[charPointer].isalnum() or string[charPointer] == '-':
            num = ''
            while charPointer < len(string) and (string[charPointer].isalnum() or string[charPointer] == '-'):
                num = num + string[charPointer]
                charPointer = charPointer + 1
            if len(num) > 0:
                row.append(num)
                if len(num) > longest:
                    longest = len(num)
        elif string[charPointer] == ';':
            m.append(row)
            row = []
            charPointer = charPointer + 1
        else:
            charPointer = charPointer + 1
    
    if len(row) > 0:
        m.append(row)
    print()
    print(toString(m, longest))

def toString(matrix, longest):
    string = ''
    for row in matrix:
        string = string + '[ '
        for entry in row:
            spaces = longest - len(entry)
            front = spaces // 2
            end = spaces - front
            string = string + (' ' * front) + entry + (' ' * end )
            string = string + ' '
        string = string + ']\n'
    
    return string