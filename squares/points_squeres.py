import matplotlib.pyplot as plt

input_values = list(range(1, 100))
squares = [x**2 for x in input_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.tab10, s=10)

ax.set_title("Квадраты чисел", fontsize=20)
ax.set_xlabel("Значения", fontsize=10)
ax.set_ylabel("Значения квадратов", fontsize=10)
# Размер шрифта делений для обоих осей
ax.tick_params(axis='both', which='major', labelsize=5)

ax.axis([0, 110, 0, 10000])

# 1 Вывод диаграммы
# plt.show()

# 2 Сохранение диаграммы в файле с отсечением лишнего пространства
plt.savefig('point_squares.png', bbox_inches='tight')