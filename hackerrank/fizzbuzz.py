def fizzBuzz(n):
    # Write your code her

    for i in range(n):
        if i/3==0 and i/5==0:
            print("FizzBuzz")
        elif i/3==0 and i/5!=0:
            print("Fizz")

n=int(input("number"))

fizzBuzz(n)