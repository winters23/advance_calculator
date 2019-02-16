import re
txt="The rain is in Spain"
x=re.search("^The.*Spain$",txt)
print(x)