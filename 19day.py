# Day 19 - 30DaysOfPython Challenge
# Syntax
#open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
#    "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
#    "a" - Append - Opens a file for appending, creates the file if it does not exist
#    "w" - Write - Opens a file for writing, creates the file if it does not exist
#    "x" - Create - Creates the specified file, returns an error if the file exists
#    "t" - Text - Default value. Text mode
#    "b" - Binary - Binary mode (e.g. images)
""" 
#Opening Files for Reading
f = open('./hola_a_todos.rtf')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
#read()
txt = f.read()
print(type(txt))
print(txt)
f.close() 
txt = f.read(10) #los 10 primeros caracteres
print(type(txt))
print(txt)
f.close()
#readline()
line = f.readline()
print(type(line))
print(line)
f.close()
#readlines()
lines = f.readlines() #o lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
#para cerrar de forma automatica
with open('./hola_a_todos.rtf') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

#Opening Files for Writing and Updating
with open('./hola_a_todos.rtf','a') as f:
    f.write('This text has to be appended at the end')
with open('./files/writing_file_example.txt','w') as f: #ete metodo crea el fichero si no existe
    f.write('This text will be written in a newly created file')

#Deleting Files
import os
os.remove('./hola_a_todos.rtf')
#si no existe nos dará un error por ello que:
import os
if os.path.exists('./hola_a_todos.rtf'):
    os.remove('./hola_a_todos.rtf')
else:
    print('The file does not exist')

#File Types
    #txt
    #JSON(JavaScript Object Notation): it is a stringified JavaScript object or Python dictionary.
    # dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
#Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
#Changing Dictionary to JSON
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json)) #JSON does not have type, it is a string type.
print(person_json)

#Saving as JSON File
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

    #File with csv Extension:CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database.
    # CSV is a very common data format in data science.
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

        #xlsx
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)"""

    #xml:XML is another structured data format which looks like HTML. In XML the tags are not predefined. 
    # The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute. 
""" <?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>

import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
 """

#EJERCICIOS
#level1
""" def speech_lines(s):
    lineas=os.read().splitlines()
    os.close()
    return 'El speech es de :',{s}, len(lineas)
    
os=open('./data/obama_speech.txt')
print(speech_lines(os))

import json

def top_10_languages(path, number):
    # 1. Cargamos los datos correctamente
    with open(path, encoding='utf-8') as f:
        countries_data = json.load(f)
    
    all_langs = []
    # 2. Extraemos todos los idiomas en una sola lista plana
    for country in countries_data:
        all_langs.extend(country['languages'])
    
    # 3. Contamos las frecuencias usando un diccionario
    counts = {}
    for lang in all_langs:
        counts[lang] = counts.get(lang, 0) + 1
    
    # 4. Ordenamos el diccionario por sus valores (frecuencia) de mayor a menor
    # sorted devuelve una lista de tuplas (PARA PODER ORDENARLOS)
    sorted_langs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_langs[:number]

print(top_10_languages('./data/countries_data.json', 10))
    

def top_populated(path, number):
    with open(path, encoding='utf-8') as f:
        countries_data = json.load(f)
    data_list = []
    for country in countries_data:
        data_list.append({
            'country': country['name'],
            'population': country['population']
        })
    sorted_pop = sorted(data_list, key=lambda x: x['population'], reverse=True)    
    return sorted_pop[:number]

print(top_populated('./data/countries_data.json', 10)) 
    
#level2
import re
emails=open('./data/email_exchanges_big.txt')
emails = emails.read()
mensajes=re.findall(r'\S*@\S*',emails)
print(mensajes)
"""
import re
def top_words(path, number):
    with open(path, encoding='utf-8') as f:
        x = f.read().lower()
    x=re.findall(r'\w+',x,re.I)
    conteo_dict = {}
    for palabra in x:
        conteo_dict[palabra] = conteo_dict.get(palabra, 0) + 1
    
    # 4. Convertimos a lista de tuplas (frecuencia, palabra) para ordenar
    # Queremos (frecuencia, palabra) para que el .sort() use el número primero
    lista_final = [(freq, pal) for pal, freq in conteo_dict.items()]
    
    # 5. Ordenamos de mayor a menor
    lista_final.sort(reverse=True)
    
    return lista_final[:number]

print(top_words('./hola_a_todos.rtf', 3))

print(top_words('./data/obama_speech.txt',10))

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
def similarities(path1,path2):
    with open(path1, encoding='utf-8') as f:
        x1 = f.read().lower()
    with open(path2, encoding='utf-8') as f:
        x2 = f.read().lower()
    x1=re.findall(r'\w+',x1,re.I)
    x2=re.findall(r'\w+',x2,re.I)
    #stop words
    stop_set = set(stop_words)
    #para filtrar:
    x1 = [p for p in x1 if p not in stop_set]
    x2 = [p for p in x2 if p not in stop_set]
    #similarity
    set1=set(x1)
    set2=set(x2)
   # Palabras que están en AMBOS discursos
    interseccion = set1.intersection(set2)
    
    # Una métrica común: (comunes / total de palabras únicas totales)
    union = set1.union(set2)
    similitud = (len(interseccion) / len(union)) * 100

    return f'Tienen una similitud del: {similitud:.2f}%'

print(similarities('./data/obama_speech.txt','./data/michelle_obama_speech.txt'))
    
import re
csv=open('./data/hacker_news.csv')
csv=csv.read()
lineas_pP=re.findall(r'^.*[Pp]ython.*$',csv,re.MULTILINE)#Multiline para que se active en cada salto de linea
print(len(lineas_pP))
java_not_js = re.findall(r'^.*Java(?!script).*$', csv, re.MULTILINE)
print(len(java_not_js))
    

    

