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
for e_dict in all_dicts:
    mag = e_dict['properties']['mag']
    lon = e_dict['geometry']['coordinates'][0]
    lat = e_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])
# Наносим данные на карту
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
    },
}]

my_layout = Layout(title='Глобальные землетрясения')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='g_e.html')

