class matrixSyntaxError(Exception):
    pass

class matrix:
    """
    A class for building and working with 2D matrices.
    
    Attributes
    data: 2D list used to store rows and columns.
    rows: Number of rows in the matrix.
    columns: Number of columns in the matrix.
    label: The name ('label') of the matrix.
    
    Methods:
    __init__: By default, generate a 0 by 0 matrix called A1. 
    buildFrom: build a matrix from an input string.
    getRow: Return the specified row as a row matrix.
    getColumn: Return the specified column as a column matrix.
    iterRow: Generate an iterator object that iterates by row.
    iterColumn: Generate an iterator object that iterates by column.
    buildRow: Generate an iterator object that builds the matrix by row.
    buildColumn: Generate an iterator object that builds the matrix by column.
    pr: Print an informative description of the matrix. For Debugging.
    __str__: Return a formatted string version of the matrix. 
    
    """
    
    def __init__(self, m=0, n=0, name='A1'):
        """
        Initializes the matrix. If m or n are not zero, the matrix is initialized with zeroes.
        """
    
        self.rows = m
        self.columns = n
        self.label = name
        self.data = []
        
        for i in range(m):
            tempRow = []
            for j in range(n):
                tempRow.append(0)
            self.data.append(tempRow)
    
    
    def buildFrom(self, inString):
        """
        Builds a matrix from an input string.
        
        The self.rows, self.columns, and self.data attributes are reset and assigned to situationally correct values given the input string.
        """
        
        #We don't edit object attributes until string is successfully parsed
        matrix = []
        columns = 0
        
        #Parse input string
        inString = inString + ';'
        inIterator = 0
        row = []
        while inIterator < len(inString):
            if inString[inIterator].isspace() or inString[inIterator] == ',':
                inIterator = inIterator + 1
                continue
                
            elif inString[inIterator] == ';':
                #validate each row is of equal length
                
                if len(row) == 0:
                    #Prevents errors on ;; 
                    pass
                elif columns == 0:
                    matrix.append(row)
                    columns = len(row)
                elif len(row) == columns:
                    matrix.append(row)
                else:
                    raise matrixSyntaxError
                        
                inIterator = inIterator + 1
                row = []
                
            else:
                entry = ''
                while inIterator < len(inString) and (inString[inIterator].isalnum() or inString[inIterator] == '-' or inString[inIterator] == '.'):
                    entry = entry + inString[inIterator]
                    inIterator = inIterator + 1
                row.append(entry)
        
        #Reset matrix attributes.
        self.data = matrix
        self.columns = columns
        self.rows = len(matrix)
    
    
    def getRow(self, num):
        """
        Return the row matrix of the specified row. Rows begin at 1
        """
        returnMatrix = matrix()
        
        if num > 0 and num <= self.rows:
            returnMatrix.data.append(self.data[num-1])
            return returnMatrix
    
    
    def getColumn(self, num):
        """
        Return the column matrix of the specified column. Columns begin at 1
        """
        returnMatrix = matrix()
        
        if num > 0 and num <= self.columns:
            for row in range(self.rows):
                tempRow = self.data[row][num-1]
                returnMatrix.data.append(tempRow)
            return returnMatrix
    
    
    def iterRow(self):
        iterable = iterMatrix(self.data, 'row')
        return iterable
    
    
    def pr(self):
        print()
        print("Displaying Matrix", self.label, "of size", self.rows, 'by', self.columns)
        print(self.data)

class iterMatrix:
    """
    An iterable helper class
    
    When the iterRow or iterColumn methods are called on a matrix object, an instance of the iterMatrix class is returned. The iterMatrix class 
    supports either row or column iteration (return the entries in a matrix row by row or column by column)
    """
    def __init__(self, data, mode):
        self.data = data
        self.mode = mode
        self.rows = len(data)
        self.columns = len(data[0])
        self.place = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.mode == 'row':
            if self.place < (self.rows * self.columns):
                temp = self.data[self.place // self.columns][self.place % self.columns]
                self.place = self.place + 1
                return temp
            else:
                raise StopIteration