class matrixSyntaxError(Exception):
    pass

class matrix:
    def __init__(self, inString):
        self.data = []
        
        #Parse input string
        inIterator = 0
        row = []
        while inIterator < len(inString):
            if inString[inIterator].isspace() or inString[inIterator] == ',':
                inIterator = inIterator + 1
                continue
                
            elif inString[inIterator] == ';':
            
                #validate each row is of equal length
                if len(self.data) == 0:
                    self.data.append(row)
                    self.columns = len(row)
                elif len(row) == self.columns:
                    self.data.append(row)
                else:
                    raise matrixSyntaxError
                        
                inIterator = inIterator + 1
                row = []
                
            else:
                entry = ''
                while inIterator < len(inString) and (inString[inIterator].isalnum() or inString[inIterator] == '-'):
                    entry = entry + inString[inIterator]
                    inIterator = inIterator + 1
                row.append(entry)
        
        #Loop breaks when inIterator == len(inString). If last character in input string isn't ;, then the last row wont be added to self.data. 
        if len(row) == self.columns:
            self.data.append(row)
        else:
            raise matrixSyntaxError
            
    def pr(self):
        return self.data