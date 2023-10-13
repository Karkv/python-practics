#the two letters of the English alphabet are given . Display a string that includest , in order, a all\letters of the alphabet from the gine first letter to the last one

first= input("The first")
last=input("The last")

while first<=last:
    print(first,end='')

    first=chr(ord(first)+1)

print()