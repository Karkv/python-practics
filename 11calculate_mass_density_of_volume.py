result = None
flag = input("What to calculate:?(m,d,v):")
if flag=='m':
    d=float(input("Density: "))
    v = float(input("Volume:"))
    result =d*v #mass
elif flag =='d':
    m=float(input("mass"))
    v=float(input("volume"))
    result=m/v
elif flag=='v':
    m=float(input("Mass:"))
    d=float(input("Density:"))
    resulf= m/d 

print(%)
