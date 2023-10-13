class Karan:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):
        return f"{self.fname}{self.lname}"
    
p2=Karan("Karan ","Vishwakarma(*/ω＼*)☆*: .｡. o(≧▽≦)o .｡.:*☆(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)")
print(p2)


p1=Karan("Karan","Vishwakarma")
print(p1.fname)
print(p1.lname)   