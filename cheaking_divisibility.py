# Two Interger are entered. Check if the first number is evenly divisible by the second . if not, find the remainder.

a= int(input("value"))
b= int(input("values"))

if a%b==0:
    print("YES")
else:
    print("NO")
    print("THe Remainder is ", a%b)