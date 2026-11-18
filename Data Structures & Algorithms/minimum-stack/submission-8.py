class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            if self.minStack[-1] >= val: 
                self.minStack.append(val)
            self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:    
            self.minStack.pop(-1) 
        self.stack.pop(-1) 
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
      
        if self.minStack is not None: 
            return self.minStack[-1]



        """
min.      -2, 
stack.    -2, -2, -3,





        """
        
