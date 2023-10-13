goods={
    "apple":34,
    "banana":32,
    "orange":12,
    "pineapple":37,
    "cherry":31

}

for good,price in goods.items():
    print(good,"=",price)

cost=0

while True:
    good=input("What? (n-Nothing)")
    if good == "n ":
        break
    qty =int(input("How many?"))
    cost=cost+goods[good]*qty

print("Price:",cost)