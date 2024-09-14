class hashmap:
    def __init__(self,size = 100):
        self.size = size
        self.buckets = [[] for i in range(size)]
    
    def hash_function(self,key):
        return sum(ord(x) for x in str(key))%self.size
        
    def add(self,key,value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))
    
    def contains(self,key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k == key:
                return v
        return None
        
    def remove(self,key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
            
    
    def print_LL(self):
        for index,bucket in enumerate(self.buckets):
            print(f"{index}:{bucket}")

h = hashmap()
h.add('nihala','hello')
h.add('lahani','hi')
h.add('apple','so')
h.add('orange','yy')
h.remove('nihala')
print(h.contains('nihala'))
h.print_LL()