from plotly.graph_objs import Bar, Layout
from plotly import offline

from cube import Cube

cube = Cube()
# Моделируем броски и сохраняем результаты в списке
results = []
for roll_num in range(1000):
    result = cube.roll()
    results.append(result)

    # Анализ результатов
frequencies = []
for value in range(1, cube.num_sides+1):
    frequensy = results.count(value)
    frequencies.append(frequensy)

    # Визуализация резуьтатов
x_values = list(range(1, cube.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Результат'}
y_axis_config = {'title': 'Частота результатов'}

my_layout = Layout(title='Результат броска n -е количество раз', xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

print(frequencies)
