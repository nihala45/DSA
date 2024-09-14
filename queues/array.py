class queue:
    def __init__(self):
        self.q1 = []
        
    def enequeue(self,data):
        self.q1.append(data)
        
    def dequeue(self):
        if self.is_empty():
            return 'this is an empty path'
        self.q1.pop(0)
        
    def is_empty(self):
        return len(self.q1)==0

q = queue()
q.enequeue(1)
q.enequeue(2)
q.enequeue(3)
q.enequeue(4)
q.enequeue(5)

# q.dequeue()
# q.dequeue()
print(q.q1)