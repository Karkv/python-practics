cars={}
print(cars)
print(type(cars))
print()


car_1={'make':'BMW','Speed':'fast'}
car_2={'make':'Mercedes','Speed':'good'}
car_3={'make':'Porsche','Speed':'Very Fast'}


cars['car1']=car_1
cars['car2']=car_2
cars['car3']=car_3

print(cars)
print()

from pprint import pprint

pprint(cars)

print()
print(cars['car1']['make'])
print(cars['car2']['make'])