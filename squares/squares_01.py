import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8]
squares = [1, 4, 9, 16, 25, 36, 49, 64]

plt.style.use('bmh')
fig, ax = plt.subplots()
# Толщина линии
ax.plot(input_values, squares, linewidth=4)
# Название диаграммы и размеры ее элементов
ax.set_title("Квадраты чисел", fontsize=20)
ax.set_xlabel("Значения", fontsize=10)
ax.set_ylabel("Значения квадратов", fontsize=10)
# Размер шрифта делений для обоих осей
ax.tick_params(axis='both', labelsize=10)

plt.show()