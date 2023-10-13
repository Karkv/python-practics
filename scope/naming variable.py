x=int(input("Enter the value"))

def myfun():
    x=34
    print(x)
    def my():
        print(x)
        def k():
            print(x)
        k()
    my()

myfun()

print(x)