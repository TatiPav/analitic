from plotly.graph_objs import Bar, Layout
from plotly import offline

from cube import Cube

cube_1 = Cube()
cube_2 = Cube()

# Моделируем броски и сохраняем результаты в списке
results = []
for roll_num in range(1000):
    result = cube_1.roll() + cube_2.roll()
    results.append(result)

    # Анализ результатов
frequencies = []
max_result = cube_1.num_sides + cube_2.num_sides
for value in range(2, max_result+1):
    frequensy = results.count(value)
    frequencies.append(frequensy)

    # Визуализация резуьтатов
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Результат', 'dtick': 1}
y_axis_config = {'title': 'Частота результатов'}

my_layout = Layout(title='Результат броска двух кубов  n -е количество раз', xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

print(frequencies)
