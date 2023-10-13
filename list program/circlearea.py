def circle_area(r):
    pi=3.14
    return pi*r

r=int(input("Enter the  r value:"))
print(circle_area(r))

for i in range(1,11):
    for j in range(1,11):
        print("%4d"%(i*j),end="")
    print()