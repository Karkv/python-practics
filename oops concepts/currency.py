class currency:
    def __next__(self):
        n=self.counter
        self.counter+=1
        if self.counter>2:
            raise StopIteration
        
        if n==0:
            return self.pad0(self.total//100)
        
    def __iter__(self):
        self.counter=0
        return self
    
    def pad0(self,n):
        if n<10:
            return "0{0}".format(n)
        return "{}".format(n)
    def __init__(self,rs,paise):
        self.total=rs*100+paise

    def __str__(self):
        r=self.totol//100
        p=self.total%100
        r=self.pad0(r)
        p=self.pad0(p)
        return "₹ {}.{}".format(r,p)
    
    def __add__(self,other):
        return currency(0,self.total+other.total)
    def __gt__(self,other):
        return self.total>other.total
    
    def __le__(self,other):
        return self.total<=other.total
    def __getitem__(self,item):
        if item==0:
            return self.