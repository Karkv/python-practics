def generator_function():
    print("Before yield")
    yield 20
    print("befor karan ")
    yield 45


for value in generator_function():
    print(value )

