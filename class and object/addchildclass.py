class person:
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln

    def printname(self):
        print("My name is {} {}.".format(self.fn,self.ln))

class stdent(person):
    def __init__(self,fn,ln):
        super().__init__(fn,ln)
        self.dob="15/02/2000"

name="karan"
Lname="vishwakarma"

x=stdent(name,Lname,)
x.printname()
print(x.dob)