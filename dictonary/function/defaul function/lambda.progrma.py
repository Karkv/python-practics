nums=[1,2,3,4,5,6,7,8,9,10]
print("find odd and even")
print(nums)

print("\nEven numbers from the said list")
even_nums=list(filter(lambda x:x%2==0,nums))
print(even_nums)
odd_nums=list(filter(lambda x:x%2!=0,nums))
print(odd_nums)

