a=int(input("Enter the value "))
b=int(input("Enter the value "))

while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=b

gcd=a+b 
print(gcd)