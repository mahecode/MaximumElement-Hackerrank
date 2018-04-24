class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def pop(self):
        if(len(self.stack)<=0):
            return False
        else:
            self.stack.pop()
    def max(self):
        print(max(self.stack))
    
    def peek(self):
        return(self.stack[0])

    
stk = Stack()
loop = int(input())
i = 0
while(i < loop):
    choice = input("").strip().split()
    if(choice[0] == '1'):
        stk.add(int(choice[1]))
    if(choice[0] == '2'):
        stk.pop()
    if(choice[0] == '3'):
        stk.max()
    i = i + 1
