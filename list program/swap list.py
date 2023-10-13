a=[] 
n=int(input("Enter the number of element in list"))

for x in range(0,n+1):
    element=int(input("enter element"+str(x+1)+":"))
    a.append(element)

temp=a[0]
a[0]=a[n-1]
a[n-1]=temp

print("new list is: ")

print(a)