class MultiplyOperation:
    num1 = 0
    num2 = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def getResult(self):
        return self.num1 * self.num2
    
    def getModuleName(self):
        return __name__
    
if __name__ == "__main__":
    multiplyOperationInstance = MultiplyOperation(3, 4)
    print(f"""
            Running from Multiply.py
            __name__ = {multiplyOperationInstance.getModuleName()}
            result  = {multiplyOperationInstance.getResult()}
          """)
else:
    multiplyOperationInstance = MultiplyOperation(7, 8)
    print(f"[NOTE] multiply.py is not the main module, (__name__ = { multiplyOperationInstance.getModuleName() })")
    