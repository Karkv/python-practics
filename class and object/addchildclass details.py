class Person:
    def __init__(self,name ,school):
        self.name=name
        self.school=school
     

    def printdetails(self):
        print("Hello! My name is {} and I studing in {} . my date of birth is ".format(self.name ,self.school))

class std(Person):
    def __init__(self,name,school,dob):
        super().__init__(name,school)
        self.dob=dob

x=std("Karan","K.K. inter college","15/02/2000")
x.printdetails()
print(x.dob)