input_filename = 'files/country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        print(country_dict)
        countries[country.casefold()] = country_dict

# print(countries)

while True:
    user_choose = input("What country you want to know about?: ").casefold()
    if user_choose in countries:
        user_country = countries[user_choose]
        print(f"The capital of {user_choose} is {user_country['capital']}")
    elif user_choose == 'quit':
        break
