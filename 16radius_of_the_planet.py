

r=float(input("Radius of the orbit(Million km): "))
v=float(input("Orbital speed (KM/s): "))
pi=3.14
r=r*1000000
year=2*pi*r/v

year=year/(60*60*24)

print(round(year))