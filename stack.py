class StackByList:
    def __init__(self):
        self.stack=[]
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            raise Exception("栈为空")
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack)==0
    
stack=StackByList()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.peek())
