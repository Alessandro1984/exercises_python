def cagr_berechnung(AK, t, EK):
    AK = abs(AK)
    t = abs(t)
    cagr = (EK/AK)**(1/t)-1
    return cagr

x = cagr_berechnung(100, 30, 700)

print(x*100)

AK = 120
t = 30

EK_2 = AK * (1 + x)**t

print(EK_2)
