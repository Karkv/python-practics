class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
        
m=mynumbers()
myiter=iter(m)

for x in myiter:
    print(x)