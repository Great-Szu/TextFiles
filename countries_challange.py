import csv
from csv import DictReader

country_dict = {}

filename = 'files/country_info.txt'

with open(filename, 'r', encoding='utf-8') as countries_file:
    reader = DictReader(countries_file, delimiter='|')
    for row in reader:
        country_name = row['Country']

        country_dict[country_name] = {
            'capital': row['Capital'],
            'country_code': row['CC'],
            'cc3': row['CC3'],
            'dialing_code': row['IAC'],
            'timezone': row['TimeZone'],
            'currency': row['Currency'],
        }

for country, data in country_dict.items():
    print(f'{country}:')
    for key, value in data.items():
        print(f' {key}: {value}')
    print()