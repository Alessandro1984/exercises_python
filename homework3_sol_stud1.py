def buchstaben_häufigkeit(word):
    res = {}
    sorted_word = sorted(word.lower())
    for letter in sorted_word:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        if letter in res:
            res[letter] += 1
        else:
            res[letter] = 1
    return res

my_diction = buchstaben_häufigkeit('Hall o123 BBB)/%§')

print(my_diction)
