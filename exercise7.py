def buchstabe_zählen(x):
    x_list = list(x)
    x_buch = [i for i in x_list if i.isalpha()]
    return len(x_buch)

print(buchstabe_zählen("Hello, Berlin%&!!"))

def buchstabe_zählen2(x):
    x_list = list(x)
    x_buch = []
    
    for i in x_list:
        if i.isalpha():
            x_buch.append(i)
    
    return len(x_buch)

print(buchstabe_zählen2("Hello, Berlin%&!!"))
