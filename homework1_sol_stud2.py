import matplotlib.pyplot as plt

# This should be the inputs of the function
AK = 10000
SR = 1000
i = 0.07
lz = 10
# Empty lists should be defined inside the function
entw_GK = []
entw_zinsen = []
entw_zinseszins = []

def spar_funktion (AK, SR, i, lz):
    for k in range (1, lz + 1):
        #ZInsen auf das bestehende Kapital
        Zinsertrag = AK * i
        #AK neu
        AK = AK + Zinsertrag + SR
        #liste hinzufügen
        entw_GK.append(round(AK, 2))
        entw_zinsen.append(round(Zinsertrag, 2))
        if k > 1:
            zinseszins = Zinsertrag * i
            entw_zinseszins.append(round(zinseszins, 2))
        else:
            zinseszins = 0
            entw_zinseszins.append(zinseszins)
    # We need a return statement that returns the lists
    # entw_GK, entw_zinsen, entw_zinseszins
    print(entw_GK)
    print(entw_zinsen)
    print(entw_zinseszins)

# spar_funktion(AK = 10000, SR = 1000, i = 0.07, lz = 10)
spar_funktion(AK, SR, i, lz)

x_werte = list(range(1, lz + 1))

gesamt_entw_plot = plt.bar(x_werte, entw_GK)
plt.xlabel("Jahre")
plt.ylabel("Kapital")
plt.show()

gesamt_zins_plot = plt.bar(x_werte, entw_zinsen)
plt.xlabel("Jahre")
plt.ylabel("Zinsen")
plt.show()
