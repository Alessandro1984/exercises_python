def buchstaben_ändern(string, buchstabe):

    vocali = ["a", "e", "i", "o", "u"]

    def buchstaben_ändern1(x, y, z):
        x_list = list(x.lower())

        for i in range(len(x_list)):
            if x_list[i] == y:
                x_list[i] = z
        return "".join(x_list)

    for i in vocali:
        print(buchstaben_ändern1(x = string, y = buchstabe, z = i), end = " ")

print(buchstaben_ändern(string = "Wie geht es Ihnen?", buchstabe = "e"))
