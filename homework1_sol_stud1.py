import matplotlib.pyplot as plt

def sparfunktion (AK,SR,I,lz):
    AK= abs(AK)
    SR= abs(SR)
    I= abs(I)
    lz= abs(lz)

    entwicklungsliste= []

    for jahr in range (1, lz+1):
        # This formula can be simplified
        endkapital = (AK*(1+I)**jahr)+(SR*((1+I)**jahr-1)/I)
        endkapital = round(endkapital,2)
        entwicklungsliste.append(endkapital)

    return entwicklungsliste

ergebnis = sparfunktion(10000,1000,0.01,10)
print(ergebnis)
plt.plot(ergebnis)
