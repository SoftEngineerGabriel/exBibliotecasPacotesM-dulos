#8. Escreva um programa que importe o pacote matplotlib e plote a função seno.

import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()