quad_zahl = []

for zahl in range(1, 11):
    if zahl % 2 == 0:
        quad_zahl.append(zahl)
    else:
        quad_zahl.append(zahl**2)

print(quad_zahl)

quad_zahl2 = [zahl if zahl%2 == 0 else zahl**2 for zahl in range(1, 11)]

print(quad_zahl2)
