weight =int(input("weight: "))
unit =  input("(L)bs or (K)g:")
if unit.upper() == "L":
    convert=weight*0.45
    print(f"You are {convert} kilos")
else:
    convert=weight/0.45
    #use of formatted strings
    print(f"You are {convert} pounds")