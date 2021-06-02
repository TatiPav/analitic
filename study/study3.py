import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Изучение структуры представленных данных
filename = 'data/day_m1.json'
with open(filename) as f:
    # Преобразование в удобный формат (словарь)
    all_data = json.load(f)
all_dicts = all_data['features']

mags, lons, lats = [], [], []
for dict in all_dicts:
    mag = dict['properties']['mag']
    lon = dict['geometry']['coordinates'][0]
    lat = dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])
# Наносим данные на карту
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Глобальные землетрясенея')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='g_e.html')



