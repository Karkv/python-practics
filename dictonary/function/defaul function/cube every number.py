num=[1,2,3,4,5,6,7,8,9,10]
print("Orginal list of integers")
print(num)
print("\nsquare every number of the said list:")
squre_num=list(map(lambda x:x**2,num))
print(squre_num)
print("\n cube every number of the said list:")
cube_num=list(map(lambda x:x**3,num))
print(cube_num)