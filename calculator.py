from add import AddOperation
from multiply import MultiplyOperation

class Calculator:
    num1 = 0
    num2 = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def getResult(self):
        addOperationInstance =  AddOperation(self.num1, self.num2)
        addResult = addOperationInstance.getResult()
        multiplyOperationInstance = MultiplyOperation(addResult, addResult)
        multiplyOperationResult = multiplyOperationInstance.getResult()
        return multiplyOperationResult

if __name__ == "__main__":
    calculatorInstance = Calculator(10, 20)
    print(f"""
            Running from calculator.py
            __name__ = {__name__}
            result  = {calculatorInstance.getResult()}
          """)
    
    