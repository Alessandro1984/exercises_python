def buchstaben_ändern(string, buchstabe):
    vokale = "aeiou"
    string = string.lower()
    new_strings = []

    for i in vokale:
        new_word = "".join(char if char != buchstabe else i for char in string)
        new_strings.append(new_word)
    print(new_strings)

buchstaben_ändern("Wie geht es Ihnen", "e")
