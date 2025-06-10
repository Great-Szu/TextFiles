import csv

country_dict = {}

filename = 'files/country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'


with open(filename, 'r', encoding='utf-8') as countries_file:
    # Get the column headings from the first line of the file
    headings = countries_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    reader = csv.DictReader(countries_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        country_name = row['Country']
        print(row)
        country_dict[country_name] = {
            'capital': row['Capital'],
            'country_code': row['CC'],
            'cc3': row['CC3'],
            'dialing_code': row['IAC'],
            'timezone': row['TimeZone'],
            'currency': row['Currency'],
        }

# for country, data in country_dict.items():
#     print(f'{country}:')
#     for key, value in data.items():
#         print(f' {key}: {value}')
#     print()