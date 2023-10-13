def celsiusconvert(fr):
    cel=(fr/1.8)-32
    print(cel)

def fahrenheitconvert(c):
    fer=(c*1.8)+32
    print(fer)



fr=int(input("Enter the value of fahrenheit : "))
c=int(input("Enter the value of Celsius : "))


celsiusconvert(fr)
fahrenheitconvert(c)