#if you need to create a global variable but are stuck in the localscope,you can use the global keyword.

def func():
    global x
    x=3434
    def nd():
        x=4
        print(x)
    nd()
func()
print(x)