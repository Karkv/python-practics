x=input("inter the string:")

count1=0
count2=0

for i  in x:
    if (i.isdigit()):
        count1+=1

    count2+=1

print("The number of digits is : ",count1)
print("The number of character is : ",count2)