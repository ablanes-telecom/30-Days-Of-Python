# Day 20 - 30DaysOfPython Challenge
"""
import numpy
print(numpy.version.version)
lst = [1, 2, 3,4, 5]
np_arr = numpy.array(lst)
print(np_arr)
len(np_arr)
print(np_arr * 2)
print(np_arr  + 2)

import pandas
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

#para desinstalarse packages: pip3 uninstall nombrepaquete
#para ver la lista de paquetes instalados: pip3 list
#para ver la info de un paquete: pip show packagename
#para saber mas detalles del paquete: pip show --verbose pandas
#pip freeze: para gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.

#Reading a url:pip3 install requests

We will see get, status_code, headers, text and json methods in requests module:

    get(): to open a network and fetch data from url - it returns a response object
    status_code: After we fetched data, we can check the status of the operation (success, error, etc)
    headers: To check the header types
    text: to extract the text from the fetched response object
    json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

#Creating a package: A package is actually a folder containing one or more module files.
from mypackage import arithmetic
print(arithmetic.add_numbers(1, 2, 3, 5))
from mypackage import greet
print(greet.greet_person('Asabeneh', 'Yetayeh'))

#al final hay +info sobre paquetez
"""

#EJERCICIOS


import requests # web browser module to open websites
import re
# list of urls: python
url = 'http://example.com'
response = requests.get(url)
txt= response.text

def top_words(x):
    x=re.findall(r'\w+',x,re.I)
    conteo_dict = {}
    for palabra in x:
        conteo_dict[palabra] = conteo_dict.get(palabra, 0) + 1
    # 4. Convertimos a lista de tuplas (frecuencia, palabra) para ordenar
    # Queremos (frecuencia, palabra) para que el .sort() use el número primero
    lista_final = [(freq, pal) for pal, freq in conteo_dict.items()]
    # 5. Ordenamos de mayor a menor
    lista_final.sort(reverse=True)
    return lista_final[:10]
print(top_words(txt)) #está contando todo el html (el código)

import statistics
url='https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
gatos = response.json()
pesos=[]
for i in gatos:
    dato=i['weight']['metric']
    partes = dato.split(" - ")
    numeros=[int(n.strip()) for n in partes]
    media_peso = statistics.mean(numeros)
    pesos.append(media_peso)
print(min(pesos))
print(max(pesos))
print(statistics.median(pesos))
print(statistics.mean(pesos))
print(statistics.stdev(pesos))

years=[]
for i in gatos:
    dato=i['life_span']
    partes = dato.split(" - ")
    numeros=[int(n.strip()) for n in partes]
    media_anos = statistics.mean(numeros)
    years.append(media_anos)
print('El gato más joven:',min(years))
print('El gato más mayor:',max(years))
print('La media de años:',statistics.median(years))
print('La mediana de años:',statistics.mean(years))
print('La desviación:',statistics.stdev(years))

dict={}
for i in gatos:
    pais=i['country_code']
    if pais in dict:
        dict[pais] += 1
    else:
        dict[pais] = 1
print(dict)



