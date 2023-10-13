# python program to find the area of triangle


a= int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))

#Uncommnet below to take inpust form the user


#calculate the semi-perimeter
s=(a+b+c)/2

#calculate the area

area=(s*(s-a)*(s-b)*(s-c))**0.5

print("The area of the triangle is ",area)
print(type(area))