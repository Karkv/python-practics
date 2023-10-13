import os
if os.path.exists("ked.txt"):
    os.remove("ked.txt")
else:
    print("The file does not exist")