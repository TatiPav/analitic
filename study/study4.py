import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Изучение структуры представленных данных
filename = 'data/day30_m1.json'
with open(filename) as f:
    # Преобразование в удобный формат (словарь)
    all_data = json.load(f)
all_dicts = all_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for e_dict in all_dicts:
    mag = e_dict['properties']['mag']
    lon = e_dict['geometry']['coordinates'][0]
    lat = e_dict['geometry']['coordinates'][1]
    title = e_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Наносим данные на карту
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Picnic',
        'reversescale': True,
        'colorbar': {'title': 'Величина'},
    },
}]

my_layout = Layout(title='Глобальные землетрясения')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='g_e.html')

