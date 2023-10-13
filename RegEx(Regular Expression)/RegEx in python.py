import re

txt="The rain in India"
x=re.search("^The.*India$",txt)
if x:
    print("Yes ! we have a match")
else:
    print("no match")