def buchstaben_ändern(string, buchstabe):
    vokale = 'aeiou'
    buchstabe = buchstabe.lower()  # Um Groß- und Kleinschreibung zu berücksichtigen

    if buchstabe not in vokale:
        return "Bitte geben Sie einen Vokal ein."

    ersetzt_strings = [string]

    for vokal in vokale:
        if vokal != buchstabe:
            ersetzt_string = ''
            for char in string:
                # print(char)
                if char.lower() == buchstabe:
                    if char.isupper():
                        ersetzt_string += vokal.upper()
                    else:
                        ersetzt_string += vokal
                else:
                    ersetzt_string += char
            ersetzt_strings.append(ersetzt_string)

    #for i in ersetzt_strings:
    #    print(i, end = " ")
    return " ".join(ersetzt_strings)

# Beispielaufruf der Funktion
ergebnis = buchstaben_ändern(string="ElEfent", buchstabe="E")
print(ergebnis)
