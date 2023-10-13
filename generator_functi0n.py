def regular_function():
    print("INside regular function")
    return 10

print(regular_function())


def genarator_function():
    print("Before yield")  #<generator object genarator_function at 0x0000017BD8A9DE70>

    yield 20


print(genarator_function())
print(next(genarator_function()))