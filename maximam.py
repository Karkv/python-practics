#There are three variables associated with interges . Determine which of the variables contains the maximum number. Displaythe maximum of the screen


a=int(input("Enter The value:"))
b=int(input("Enter The value:"))
c=int(input("Enter The value:"))


print("the Maximum is :",end="")

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)

else:
    print(c)