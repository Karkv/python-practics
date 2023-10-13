a=[]

n= int(input("enter number of elements:"))

for i in range(1,n+1):
    b=int(input("Enter elements"))
    a.append(b)

a.sort()
print("second largest number is : ",a[n-2])

