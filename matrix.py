class matrixSyntaxError(Exception):
    pass

class matrixFullError(Exception):
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
    
    def __init__(self, m=0, n=0, data=[], name='A1'):
        """
        Constructor of matrix objects.

        If m or n are not zero, the matrix is initialized with zeroes.
        """
    
        self.rows = m
        self.columns = n
        self.data = data
        self.label = name
        
        if data == []:
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
                row.append(float(entry))
        
        #Reset matrix attributes.
        self.data = matrix
        self.columns = columns
        self.rows = len(matrix)
    
    
    def getRow(self, rowNumber):
        """
        Return the row matrix of the specified row. Rows begin at 1
        """
        
        if rowNumber > 0 and rowNumber <= self.rows:
            returnMatrix = matrix(1, self.columns)
            newData = self.data[rowNumber-1]
            returnMatrix.data = newData
            return returnMatrix
    
    
    def getColumn(self, columnNumber):
        """
        Return the column matrix of the specified column. Columns begin at 1
        """
        
        if columnNumber > 0 and columnNumber <= self.columns:
            returnMatrix = matrix(self.rows, 1)
            newData = []
            for row in range(self.rows):
                tempRow = [self.data[row][columnNumber-1]]
                newData.append(tempRow)
            returnMatrix.data = newData
            return returnMatrix
    
    
    def iterRow(self):
        """
        Returns an instance of the iterMatrix class. This instance object supports iteration through the standard Python iteration protocol. The iteration occurs row by row from top left to bottom right. 
        """
        iterable = iterMatrix(self.data, 'row')
        return iterable
    
    def iterColumn(self):
        """
        Returns an instance of the iterMatrix class. This instance object supports iteration through the standard Python iteration protocol. The iteration occurs column by columns, beginning with the top left and ending at the bottom right.
        """
        iterable = iterMatrix(self.data, 'column')
        return iterable
    
    def buildRow(m, n):
        """
        Returns an instance of the buildMatrix class. This instance supports dynamic matrix creation. Entries can be added to the matrix row by row until the matrixFullError is raised. 
        """
        builder = buildMatrix(m, n, 'row')
        return builder
    
    def pr(self):
        print()
        print("Displaying Matrix", self.label, "of size", self.rows, 'by', self.columns)
        print(self.data)
    
    def smartpr(self):
        maxLength = 0
       
        for row in range(self.rows):
            for entry in range(self.columns):
                self.data[row][entry] = str(self.data[row][entry])
                temp = len(self.data[row][entry])
                if temp > maxLength:
                    maxLength = temp 
        
        print(maxLength)
        mstring = ""
        for row in range(self.rows):
            mstring = mstring + "[ "
            for entry in range(self.columns):
                print(self.data[row][entry])
                if self.data[row][entry][0] == "-":
                    mstring = mstring + " " + self.data[row][entry] + " "* (maxLength + 1 - len(self.data[row][entry]))
                else:
                    print("here")
                    mstring = mstring + "  " + self.data[row][entry] + " "* (maxLength - len(self.data[row][entry]))
            mstring = mstring + " ]\n"
        print(mstring)
           

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
        self.end = (self.rows * self.columns)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.mode == 'row':
            if self.place < self.end:
                temp = self.data[self.place // self.columns][self.place % self.columns]
                self.place = self.place + 1
                return temp
            else:
                raise StopIteration
        elif self.mode == 'column':
            if self.place < self.end:
                temp = self.data[self.place % self.rows][self.place // self.rows]
                self.place = self.place + 1
                return temp
            else:
                raise StopIteration

class buildMatrix:
    """
    A helper class for building a matrix when the entries are not known at matrix creation time. 
    """
    def __init__(self, m, n, mode):
        self.data = []
        self.mode = mode 
        self.rows = m 
        self.columns = n 
        self.place = 0 
        self.end = (self.rows * self.columns)
        
        #Initialize to a zero matrix
        for i in range(0, self.rows):
            temp = []
            for j in range(0, self.columns):
                temp.append(0)
            self.data.append(temp)
    
    def insert(self, *entries):
        """
        Can insert an arbitrary number of arguments as entries in a matrix. Once the matrix is full, the matrixFullError is raised.
        """
        for entry in entries:
            if self.mode == 'row':
                if self.place < self.end:
                    self.data[self.place // self.columns][self.place % self.columns] = entry
                    self.place = self.place + 1 
                else:
                    raise matrixFullError
            elif self.mode == 'column':
                if self.place < self.end:
                    self.data[self.place % self.rows][self.place // self.rows] = entry
                    self.place = self.place + 1
                else:
                    raise matrixFullError
    
    def get(self):
        """
        Returns an instance of the matrix class containing a built matrix.
        """
        temp = matrix(self.rows, self.columns, self.data)
        return temp