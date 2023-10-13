import random
import math

lower=int(input("Enter the lower number:- "))

upper=int(input("Enter the upper bound:- "))

x=random.randint(lower,upper)
print("\n\tYou've only",
      round(math.log(upper-lower+1,2)),"chances to guess the interger!\n")

count=0
while count<math.log(upper-lower+1,2):
    count+=1

    guess=int(input("Guess a number:- "))

    if x==guess:
        print("Congrutulations you did it in  ",count," tye ")
        break
    elif x>guess:
        print("yes guessed to small! ")
    else:
        print("you Guessed too high! ")

if count>=math.log(upper-lower+1,2):
    print("\n the number is %d" ,x)
    print("\t Better luck Next time!")




