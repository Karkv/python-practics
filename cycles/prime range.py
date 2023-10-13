num= int(input("Enter upper limite"))

for a in range(2,num+1):
    k=0
    for i in range(2,a//2+1):
        if a%i==0:
            k=k+1

    if(k<=0):
        print(a , " is a prime number")






num= int(input("Enter the range "))

for a in range(2,num+1):
    k=0
    for i in range(2,a//2+1):
        if a%i==0:
            k=k+1
    if k<=0:
        print(a)