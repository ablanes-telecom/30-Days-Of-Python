# Day 22 - 30DaysOfPython Challenge

import requests
from bs4 import BeautifulSoup
"""
url = 'https://archive.ics.uci.edu/datasets'
response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)"""

#EJERCICIO
#1
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
status=response.status_code
#print(status)
soup = BeautifulSoup(response.content, 'html.parser')

todos_a=[]
for link in soup.find_all('a'):
    href = link.get('href') # Extraemos la dirección URL del enlace
    todos_a.append(href)

data = {
        "url": url,
        "title": soup.title.string if soup.title else "No title",
        "stats": [todos_a] 
    }
with open('./web_to_json_22.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#2
url='https://archive.ics.uci.edu/dataset/186/wine+quality'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
tabla=[]
for table in soup.find_all('table'):
    filas_de_esta_tabla = []
    for fila in table.find_all('tr'):
        # Extraemos el texto de cada celda y lo limpiamos
        celdas = [celda.get_text(strip=True) for celda in fila.find_all(['td', 'th'])]
        filas_de_esta_tabla.append(celdas) 
    tabla.append(filas_de_esta_tabla)

data = {
        "url": url,
        "title": soup.title.string if soup.title else "No title",
        "stats": tabla
    }
with open('./webtable_to_json_22.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


#3
url='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
tabla=[]
for table in soup.find_all('table',{'class': 'classwikitable sortable sticky-header'}):
    filas_de_esta_tabla = []
    for fila in table.find_all('tr'):
        # Extraemos el texto de cada celda y lo limpiamos
        #strip=True sirve para eliminar espacios en blanco sobrantes
        #Es una comprensión de listas que recorre cada celda HTML (td o th) de una fila,
        #le extrae el texto limpio de espacios y guarda todos los resultados directamente en una lista nueva llamada celdas
        celdas = [celda.get_text(strip=True) for celda in fila.find_all(['td', 'th'])]
        filas_de_esta_tabla.append(celdas) 
    tabla.append(filas_de_esta_tabla)

data = {
        "url": url,
        "title": soup.title.string if soup.title else "No title",
        "stats": tabla
    }
with open('./presidentes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# el ejercicio sigue sin salir y en teoria es tema de permisos de wikipedia o algo así
