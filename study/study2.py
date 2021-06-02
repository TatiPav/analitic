import json
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

print(mags[:10])
print(lons[:5])
print(lats[:5])



