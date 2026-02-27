# Day 10 - 30DaysOfPython Challenge
"""
#Bucle while
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

#break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
#continue
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

#for
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

#for con tuples
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

#for con strings
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

#for en diccionarios
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

#for con un set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

#break y continue funcionan de igual forma que en el de while

#the range() function  range(start, end, step) 
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

#bucles dentro de bucles
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#else con el for
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

#pass, se usa para evitar errores y no queremos ejecutar código
for number in range(6):
    pass

#EJERCICIOS
#level1
count=[0,1,2,3,4,5,6,7,8,9,10]
for i in count:
    print(i)
for i in reversed(count):
    print(i)
count=0
while count<=10:
    print(count)
    count=count+1
count=10
while count>=0:
    print(count)
    count=count-1


for i in range(1,8):
    print('#'*i)

for i in range(8):
    for j in range(8):
        print('#', end=" ")
    print()

for i in range(0,11):
    print(i*i)

lst= ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)
   
for i in range(1,100,2):
    print(i)
for i in range(0,100,2):
    print(i) 

#level2
final=0
for i in range(0,101):
    final+=i
print(final)

odd=0
even=0
for i in range(0,101):
    if i % 2 ==0: even+=i
    else: odd+=i

print(odd)
print(even)
 
#level3
fruits=['banana', 'orange', 'mango', 'lemon']
for i in reversed(fruits):
    print(i)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

#for i in countries:
 #   if 'land' in i: print(i)

from countries_data import countries
 
idiomas_unicos=set() #para que no haya duplicados
for i in countries: 
    for languages in i['languages']:
        idiomas_unicos.add(languages)

print(len(idiomas_unicos)) 

from countries_data import countries
 
conteo= {} 
for i in countries: 
    for languages in i['languages']:
        conteo[languages]= conteo.get(languages,0)+1

# Ordenamos el diccionario por valor (frecuencia) de mayor a menor
top_10_manual = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_10_manual)"""

from countries_data import countries

#Crea una nueva lista con los mismos elementos pero en un orden diferente.
#key=lambda x: x['population']: Como los elementos son diccionarios, Python 
# no sabe cómo compararlos. El lambda es una mini-función que le dice: 
# "Para decidir quién va primero, mira dentro de cada país (x) y usa el valor de la clave ['population']".
paises_ordenados = sorted(countries, key=lambda x: x['population'], reverse=True)
top_10_limpio = [{'country': p['name'], 'population': p['population']} for p in paises_ordenados[:10]]
print(top_10_limpio)


