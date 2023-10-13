def kmconvert(miles):
    kilometre=miles/0.62137
    print( "miles to converted in kilometer ",kilometre)


def milesconvert(km):
    miles=km*0.62137
    print("kilometer is converted to miles ", miles)



miles=int(input("Enter the distance in miles  "))
km=int(input("Enter the distance in kilomitter : "))


milesconvert(km)
kmconvert(miles)