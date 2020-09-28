#main.py
#Sunday, September 27, 2020
import staticMatrix
import matrixTools

class program:
    def parseInput(inputString):
        inputString = inputString.strip()
        inputString = inputString.lower()
        inputList = inputString.split()
        return inputList

    def createMatrix(self, argument):
        matrix = matrixTools.buildMatrix(argument, float)
        self.objects[self.counter] = matrix
        
        print("\nMatrix ", self.counter)
        self.counter = self.counter + 1
        print(matrix.toString())
    
    def listObjects(self):
        for (var, obj) in self.objects.items():
            print("\n Matrix: ", var)
            print(obj.toString())
        
    def main(self):
        self.objects = {}
        self.counter = 0
        
        while True:
            userInput = input("% ")
            inputList = program.parseInput(userInput)
        
            if len(inputList) == 0:
                continue
            elif len(inputList) == 1:
                command = inputList[0]
                arguments = []
            else:
                command = inputList[0]
                arguments = inputList[1:]
                
            if command == "q":
                break
            elif command == "m":
                self.createMatrix("".join(arguments))
            elif command == "l":
                self.listObjects()

p = program()
p.main()