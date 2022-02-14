from pprint import pprint

temp_city = {
    'city': 'Москва', 'temperature': '20'
}
print(temp_city['city'])
temp_city['temperature'] = int(temp_city['temperature']) - 5
pprint(temp_city)
print(temp_city.get('country'))
temp_city['country'] = 'Россия'
temp_city['date'] = '27.05.2019'
print(len(temp_city))