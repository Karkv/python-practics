'''def check(n):
    if n%2==0:
        print("EVEN ")
    else:
        print("ODD")


n=int(input("Enter the number"))

check(n)


'''
def check(n):
    if n<2:
        return n%2==0
    return (check(n-2))

n= int(input("Enter number:"))
if(check(n)==True):
    print("Number is EVEN!")
else:
    print("Number is ODD!")