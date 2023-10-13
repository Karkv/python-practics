def removeodd(string):
    finaly=" "
    for i in range(len(string)):
        if i%2==0:
            finaly=finaly+string[i]
    return finaly

string= input("Enter the string ")

print("modify strings")
print(removeodd(string))