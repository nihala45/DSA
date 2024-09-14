class hashset:
    def __init__(self,size = 100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def hash_function(self,value):
        return sum(ord(x) for x in value)%self.size
    
    def add(self,value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)
    
    def contains(self,value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    
    def remove(self,value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)
            
    def print__ll(self):
        for index,bucket in enumerate(self.buckets):
            print(f"{index}:{bucket}")
        
h = hashset()
h.add('nihala')
h.add('lahani')
h.add('hello')
h.add('example')
h.print__ll()
   