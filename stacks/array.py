class Stacks:
    def __init__(self):
        self.s1 = []
        
    def push(self,data):
        self.s1.append(data)
        
    def pop(self):
        if self.is_empty():
            return
        self.s1.pop()
    
    def is_empty(self):
        return len(self.s1) == 0
    
    
s = Stacks()  
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
print(s.s1)  