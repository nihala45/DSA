class Queue:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def enequeue(self,data):
        self.q1.append(data)
    
    def dequeue(self):
        while self.q1:
            self.q2.append(self.q1.pop())
        self.q2.pop(0)
        
q = Queue()
q.enequeue(1)
q.enequeue(2)
q.enequeue(3)
q.enequeue(4)
q.enequeue(5)
q.dequeue()
print(q.q2)