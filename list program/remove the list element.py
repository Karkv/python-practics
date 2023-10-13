def remove(k,n):
    first=k[:n]
    last=k[n+1:]
    return first+last

k=input("enter the string:")

n=int(input("Enter the number that I want to skip "))
print("Modifided string")
print(remove(k,n))