class Person:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age

    def fun(self):
        print("Hello ! my name is {} and my age {}".format(self.Name,self.Age))

p1=Person("Karan",23)
p1.fun()