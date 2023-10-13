def k(e):
    if (e > 0):
        result=e=k(e - 1)
        print(result)

    else:
        result=0
    return result

print("\n\n Recursion Example results")
k(6)