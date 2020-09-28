#staticMatrix.py
#Created on Sunday, September 27, 2020

class invalidMatrixDimensionsError(Exception):
    pass

class staticMatrix:
    """
    A class for creating immutable sized matrices. 
    
    The desired size of the matrix must be known before a matrix object is instantiated. The data inside a matrix object can change, but the size of the matrix remains fixed. This seems to be a decent compromise between entirely immutable matrices (where data is also fixed) and entirely mutable matrices (like the one specified in matrix.py). It should be easier to validate the correctness of computations when the size of the matrix is fixed. 
    
    Attributes:
        rows: The number of rows in the matrix.
        columns: The number of columns in the matrix.
        data: The information stored in a matrix.
    
    Methods:
        __init__: Intializes a matrix to the specific number of rows and columns. Entries are initialized to 0.
    
    """
    
    def __init__(self, rows, columns):
        """
        Constructor for staticMatrix objects. 
        
        The rows and columns parameters must be greater than 0, otherwise an invalidMatrixDimensionsError exception is raised. The entire matrix is preinitialized with zeroes.
        """
        
        if (rows < 1 or columns < 1):
            raise invalidMatrixDimensionsError
        
        self.rows = rows
        self.columns = columns
        
        data = []
        for row in range(self.rows):
            tempRow = []
            for column in range(self.columns):
                tempRow.append(0)
            data.append(tempRow)
        self.data = data
    
    def validate(self, data):
        """
        A helper method for validating the data attribute of a staticMatrix object. Returns True is the data is valid, else returns false. 
        
        For data to be valid, the data must be a two dimensional matrix such that the total number of rows equals self.rows, and the total number of columns equals self.columns. Furthermore, each row must be the same length. Note this means that something like [1, 2, 3] is invalid since it is not a two dimensional matrix. [[1, 2, 3]] is valid.
        """
        if len(data) != self.rows:
            return False
        
        for row in data:
            if len(row) != self.columns:
                return False
        
        return True
        
    def setData(self, data):
        """
        A method for setting the data attribute of a staticMatrix object.
        
        Note that this method will rarely be called by the end user of this library. Rather, the setData is primarily used by other methods to manipulate and create staticMatrix objects. 
        """
        
        if self.validate(data):
            self.data = data
        else:
            raise invalidMatrixDimensionsError
    
    def getRow(self, rowNumber):
        """
        Returns a new staticMatrix containing the row specified by the rowNumber parameter. 
        
        The returned matrix is a row matrix (size 1 by number of columns in the original matrix). Note that the first row is specified by rowNumber = 1. In other words, 1 not 0, corresponds to the first row. 
        """
        rowMatrix = staticMatrix(1, self.columns)
        
        if rowNumber > 0 and rowNumber <= self.rows:
            data = [self.data[rowNumber-1]]
        else:
            raise invalidMatrixDimensionsError
        
        rowMatrix.setData(data)
        return rowMatrix
    
    def getColumn(self, columnNumber):
        """
        Returns a new staticMatrix containing the column specified by the rowNumber paramter.
        
        Note that the returned matrix is a column matrix (size number of rows by 1). Furthermore, as with the getRow method, the first column begins at 1, not 0.
        
        """
        columnMatrix = staticMatrix(self.rows, 1)
        
        if columnNumber > 0 and columnNumber <= self.columns:
            data = []
            for row in self.data:
                data.append(row[columnNumber-1])
        else:
            raise invalidMatrixDimensionsError
        
        columnMatrix.setData(data)
        return columnMatrix
    
    def __str__(self):
        """
        Returns a string containing the three attributes of a staticMatrix object.
        
        This method is primarily for debugging. toString() returns a visual string representation of the staticMatrix.
        """
        string = "Matrix of size " + str(self.rows) + " by " + str(self.columns) + "\n" + str(self.data) + "\n"
        return string
    
    def toString(self):
        """
        return a fancy string representation of the staticMatrix object. 
        
        Entries are padded with spaces on the left so that each column is right aligned. Example output:
        [     1.1  43124.0  1143.0  ]
        [  -100.0  -1324.3   143.0  ]
        """
        def length(entry):
            return len(str(entry))
        
        string = ""
        rows = []
        
        for i in range(self.rows):
            rows.append("[  ")
        
        for column in range(self.columns):
            maxColumnLength = 0
            for row in range(self.rows):
                l = length(self.data[row][column])
                maxColumnLength = max(l, maxColumnLength)
            for row in range(self.rows):
                entry = self.data[row][column]
                entryString = " " * (maxColumnLength - length(entry))
                entryString = entryString + str(entry)
                rows[row] = rows[row] + entryString + "  "
        
        for i in rows:
            string = string + i + "]\n"
        return string