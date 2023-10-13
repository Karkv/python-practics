# the program "guesses " a random number from  1 to 100 inclusive./ the Person must guess this number using many tries



from random import randint

secret_num=randint(1,100)

user_num=-1
try_count=1

while secret_num!=user_num:
    print("%d try:"%try_count,end="")
    user_num=int(input("||"))
    if user_num<secret_num:
        print("too less")
    elif user_num>secret_num:
        print("too much")
    else:
        print("You guessed it!")
    dfadfadfdaaadda