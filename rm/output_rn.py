import matplotlib.pyplot as plt

from r_numbers import  RNumbers

# Строим случайное блуждение
while True:
    rn = RNumbers()
    rn.fill_numbers()

    # Наносим точки на диаграмму
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.scatter(rn.x_values, rn.y_values, s=15)

    # 1 Вывод диаграммы
    plt.show()

    # 2 Сохранение диаграммы в файле с отсечением лишнего пространства
    # plt.savefig('output.png', bbox_inches='tight')

    keep_running = input("Для выполнения нажмите 'y', а потом 'n' "
                         "для записи в файл или завершения): ")
    if keep_running == 'n':
        break



