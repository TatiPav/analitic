import json
# Изучение структуры представленных данных
filename = 'data/day_m1.json'
with open(filename) as f:
    # Преобразование в удобный формат (словарь)
    all_data = json.load(f)
all_dicts = all_data['features']
print(len(all_dicts))


# readable_file = 'data/readable.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_data, f, indent=4)
