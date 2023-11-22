import matplotlib.pyplot as plt

def buchstaben_häufigkeit(x):
    mein_d = {}
    for c in x.lower():
        if c.isalpha():
            if c not in mein_d:
                mein_d[c] = 1
            else:
                mein_d[c] += 1

    mein_d_sorted = dict(sorted(mein_d.items()))

    return mein_d_sorted

buchstaben_häufigkeit(x = "123Wie g&eht es Ihnen%$?")

bh_dict = buchstaben_häufigkeit(x = "123Wie g&eht es Ihnen%$?")
print(bh_dict)
plt.bar(bh_dict.keys(), bh_dict.values())
plt.show()
