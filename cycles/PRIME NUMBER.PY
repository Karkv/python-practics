def prime(n):
    flag=False
    if n==1:
        return (n , "is not prime ")
    elif n<1:
        for i in range(2,n):
            if n%i==0:
                flag= True
                break
        if flag:
            return (n,"is prime number")
        else:
            return (n,"is not prime number")


n= int(input("Enter the value"))

print(prime(n))