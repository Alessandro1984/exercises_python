import matplotlib.pyplot as plt

def spar_funktion(AK, SR, r, lz):
    AK = AK
    GK = []

    for k in range(1, lz+1):
        AK = SR + AK * (1 + r)
        GK.append(round(AK, 2))

    return GK

# Test
EK = spar_funktion(AK = 10000, SR = 1000, r = 0.01, lz = 10)

plt.bar(range(1, 11), EK)
# plt.show()
