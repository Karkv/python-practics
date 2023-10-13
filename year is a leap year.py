# the year is entered Determine if it is leap or usual.

year= int(input())
if year%4!=0:
    print("Not leap year")
elif year%100==0 and year%400==0:
    print("leap year")

else:
    print("not leap year")