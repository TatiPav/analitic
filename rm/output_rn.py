import matplotlib.pyplot as plt

from r_numbers import  RNumbers

# Строим случайное блуждение
while True:
    rn = RNumbers(80000)
    rn.fill_numbers()

    # Наносим точки на диаграмму
    plt.style.use('seaborn-deep')
    fig, ax = plt.subplots(figsize=(15, 10))
    point_numbers = range(rn.n_points)
    ax.scatter(rn.x_values, rn.y_values, c=point_numbers, cmap=plt.cm.prism,
               edgecolors='none', s=1)
    # Выводим первую и последнюю точки в крупном масштабе
    ax.scatter(0, 0, c='red', edgecolors='none', s=150)
    ax.scatter(rn.x_values[-1], rn.y_values[-1], c='green',
               edgecolors='none', s=150)
    # Удаление осей
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    # 1 Вывод диаграммы
    plt.show()

    # 2 Сохранение диаграммы в файле с отсечением лишнего пространства
    # plt.savefig('output.png', bbox_inches='tight')

    keep_running = input("Для выполнения нажмите 'y', а потом 'n' "
                         "для записи в файл или завершения): ")
    if keep_running == 'n':
        break



