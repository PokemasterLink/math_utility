import math

put = ""

while True:
    if put == "q":
        break
    elif put != "q":
        try:
            put = input("Was ist die operation: ")
            out = eval(put)
            print(out)
        except NameError:
            print("You messed up! Thats no mafs! ")
        except SyntaxError:
            print("Yeah you kinda messed up the formating bro...")