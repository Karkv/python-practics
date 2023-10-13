print("calculator")
print("Addition")
add=lambda a,b :a+b
print(add(3,4))
print("subtraction")
sub=lambda a,b:a-b
print(sub(44,5))
print("Multiply")
mul=lambda a,b:a*b
print(mul(10,5))
print("divide")
div=lambda a,b:a/b
print(div(55,5))
a=[1,2,3,4,5,6,7,8,9,10]
print("Origenal list")
print(ConnectionAbortedError)
print("\n Odd list")
odd_list=list(filter(lambda x:x%2!=0,a))
print(odd_list)
print("Even list")
even_list=list(filter(lambda x:x%2==0,a))
print(even_list)
print("Squre")
sqr=list(map(lambda x:x**2,a))
print(sqr)
a=[1,2,3,4,5,6,7,8,9,10]
print("odd list squre")
sqr_odd=list(filter(lambda x:x%2!=0,a))
sqr_sodd=list(map(lambda x:x**2,sqr_odd))

print(sqr_odd)
print(sqr_sodd)

z=[23,34,2,12,2,3,232,32,34]
z.sort()
print(z)

sort=list(map(lambda x:x-1,z))
print(sort)
