models=[{"Make":"Nokia","Model":216,"color":"Black"},{"Make":"MI max","Model":"2","Color":"Gold"},{"Make":"Sumsung","Model":7,"color":"Blue"}]
print("Original list of dictionaries : ")
print(models)
sorted_models=sorted(models,key=lambda x:["color"])
print("\nSorting the list of dictionries : ")
print(sorted_models)