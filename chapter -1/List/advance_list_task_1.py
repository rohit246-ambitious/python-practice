'''
count all countries which are starting with "I".
Also print all these countries in a list.
'''

countries = ["India", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Indonesia", "Ivory Coast", "Canada", "China", "Chile", "Cameroon", "Cuba", "Colombia", "United States of America","shri lanka",'poland','portugal','peru','paraguay','suoth africa','serbia','spain','sweden']
counter = 0
output_countries = []

for country in countries:
    if country.startswith("I"):
        counter +=1
        output_countries.append(country)

print("Total countries starting with 'I':", counter)
print("Countries starting with 'I':", output_countries)