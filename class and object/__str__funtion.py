class fruits:
    def __init__(self,f1,price1,f2,price2,f3,price3,f4,price4,f5,price5):
        self.f1=f1
        self.price1=price1
        self.f2=f2
        self.price2=price2
        self.f3=f3
        self.price3=price3
        self.f4=f4
        self.price4=price4
        self.f5=f5
        self.price5=price5

    def __str__(self):
        return f"{self.f1}________({self.price1})\n{self.f2}________({self.price2})\n{self.f3}________({self.price3})\n{self.f4}________({self.price4})\n{self.f5}________({self.price5})"
for i in range(5):
    items=input(Enter the items)
#fruitslist=fruits("Orange",34,"apple",120,"cherry",140,"Banana",80,"Grappess",45)
print("ITEMS________PRICE(RS)")

print(fruitslist)