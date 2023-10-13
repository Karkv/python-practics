def func(n):
    return lambda x:x*n
result=func(2)
print("Double the number of 15 =",result(15))
resutl=func(3)
print("Triple the number of 15 =",result(15))
result=func(4)
print("fourth the number of 15 =",result(15))
result=func(5)
print("fifth the number of 15 =",result(15))
result=func(6)
print("six the number of 15 =",result(15))
result=func(7)
print("seven the number of 15 =",result(15))
