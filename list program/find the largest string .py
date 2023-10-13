string1=input("Enter the first string")
string2=input("Enter the second string")

count1=0
count2=0


for i in string1:
    
    count1=count1+1
    
for j in string2:
    count2+=1

if (count1<count2):
    print("largest string is :",string2)

elif(count1>count2):
    print("largest string is  " ,string1)

else:
    print("Both string are equal.")