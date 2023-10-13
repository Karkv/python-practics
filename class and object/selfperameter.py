class Person:
    def __init__(zd,Name,Age):
        zd.Name=Name
        zd.Age=Age

    def ne(kak):
        print("my name is {} and my age {} //".format(kak.Name,kak.Age))

p1=Person("Karan",23)
p2=Person("Iqra",23)
p1.Age=34
#del p1.Age

p1.ne()
p2.ne()
