import matplotlib.pyplot as plt

a = 1
r = 0.5
s_n = []
n = 10
cumulative_sum = 0

for k in range(0, n):
    cumulative_sum += a * r**(k)
    s_n.append(cumulative_sum)

print(s_n)

x = range(0, 10)
y = s_n

plt.plot(x, y)
# plt.show()
