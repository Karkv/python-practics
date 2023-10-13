# PROGRAM TO CHECK IF A NUMBER IS PRIME OR NOT \
'''

'''
#to take input from the user

num=int(input("Enter the number"))

if num==1:
    print(num,"is not prime number")
elif(num>1):
    
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
        else:
            print(num,"is a prime number")

else:
    print(num,"is not a prime number")