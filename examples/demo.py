import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-100, 100, 30)
Y = np.arange(-100, 100, 20)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.scatter(U,V, c='orange')
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=5.5, Y=1.1, U=100,
             label='Quiver key, length = 10', labelpos='E')

# 1 Вывод диаграммы
# plt.show()

# 2 Сохранение диаграммы в файле с отсечением лишнего пространства
plt.savefig('demo.png', bbox_inches='tight')
