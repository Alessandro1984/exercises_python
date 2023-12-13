def vokon_zählen(x):
    wort = x.lower()
    count_buch = 0
    count_vok = 0
    vokalen = "aeiou"
    
    for i in wort:
        if i.isalpha():
            count_buch +=1
            if i in vokalen:
                count_vok += 1

    print(f"Es gibt {count_vok} Vokalen und {count_buch-count_vok} Konsonanten.")

vokon_zählen("HEllo$$$$56Berlin$$$")
                        