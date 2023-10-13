n = int(input("Enter the value "))

flag=False

if n==1:
    print(n,"is not prime ")

elif n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
    if flag:
        print(n ,"is a prime number")
    else:
        print(n, " is not prime")