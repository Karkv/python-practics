
n=int(input("enter the value:  "))

f1=f2=1

print(f1,f2,end=" ")

for i in range (2,n):
    f1,f2=f2,f1+f2
    print(f2,end=" ")
    i=i+1

print()