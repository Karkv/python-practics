from random import randint


counter=1

while True:
    random_n=randint(1,9)
    print("Roll",counter,"value",random_n)

    if random_n==1:
        break

    counter=counter+1