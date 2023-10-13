a=input("enter the string")

c1=0
c2=0

for i in a:
    if (i.isupper()):
        c1+=1
    elif (i.islower()):
        c2+=1

print("the numbr of uppercase -==",c1)
print("the number of lower case ==",c2)
