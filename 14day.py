# Day 14 - 30DaysOfPython Challenge
"""
#Higher Order Functions
#Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

#Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

#python closures: In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
#closure_result(5)  # 15
#closure_result(10)  # 20

#Python Decorators
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

#
# Applying Multiple Decorators to a Single Function
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

#Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')

#Built-in Higher Order Functions
#- Map function
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

#- Filter Function
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']

# - Reduce Function
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
"""
#EJERCICIOS
#level1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#map() te permite definir una funcion y sus parametros, filter igual y te da los parametros filtrados segun la funcion
#y reduce solo te da un número
#Higher orden function trata de Funciones que operan sobre otras funciones (las reciben o las devuelven).
# Una closure es una función interna que "atrapa" y recuerda variables de su entorno local superior.
#decorator es Un envoltorio que usa los dos conceptos anteriores para añadir funcionalidad a una función sin tocar su código original.
for country in countries: print(country)
for name in names: print(name)
for number in numbers: print(number)

#level2
def make_uppercase(country):
    return country.upper()
print(list(map(make_uppercase, countries)))

def square(x):          # a square function
    return x ** 2
print(list(map(square,numbers)))
def uppercase(name):
    return name.upper()
print(list(map(uppercase,names)))

def land(country):
    if 'land' in country: return True
    else: return False
print(list(filter(land,countries)))

def six(country):
    if len(country)==6: return True
    else: return False
print(list(filter(six,countries)))

def empiezan_por_e(country):
    if country.startswith('E'): return True
    else: return False
print(list(filter(empiezan_por_e,countries)))  

print(list(filter(six, map(uppercase, countries))))

def get_string_lists(list):
    if type(list) != str: return False
    else: return True
print(list(filter(get_string_lists,countries)))

from functools import reduce
print(reduce(lambda x, y: x + y,numbers))

def concatenar_paises(acumulado, pais):
    # Si es el último país de la lista, añadimos ", and "
    if pais == countries[-1]:
        return f"{acumulado}, and {pais}"
    # Para el resto, simplemente añadimos una coma
    else:
        return f"{acumulado}, {pais}"

# Aplicamos reduce y luego concatenamos el final de la frase
print(reduce(concatenar_paises, countries) + " are north European countries")

def contar_letras(acumulador, pais):
    primera_letra = pais[0].upper()
    if primera_letra in acumulador: acumulador[primera_letra] += 1
    else:
        acumulador[primera_letra] = 1
        
    return acumulador
print(reduce(contar_letras, countries, {}))

def get_first_three_countries(countries):
    return countries[0], countries[1], countries[2]
print(get_first_three_countries(countries))

#level3
from countries_data import countries
# Ordenar por nombre (Alfabético)
by_name = sorted(countries, key=lambda c: c['name'])

# Ordenar por capital
by_capital = sorted(countries, key=lambda c: c['capital'])

# Ordenar por población (De mayor a menor)
by_population = sorted(countries, key=lambda c: c['population'], reverse=True)

def ten_most_spoken_languages():
    # 1. Extraemos todos los idiomas usando map y los aplanamos
    all_langs = []
    for langs in map(lambda c: c['languages'], countries):
        all_langs.extend(langs)
    
    # 2. Contamos frecuencias usando un diccionario
    # (Usamos reduce para crear el diccionario de conteo, muy nivel Day 14)
    counts = reduce(lambda acc, lang: {**acc, lang: acc.get(lang, 0) + 1}, all_langs, {})
    
    # 3. Ordenamos por el valor (cantidad de países) y sacamos los 10 primeros
    sorted_langs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[:10]

print("Top 10 Idiomas:", ten_most_spoken_languages())
# Usamos sorted para ordenar y luego hacemos un slice [:10] para los 10 primeros
top_ten_populated = sorted(countries, key=lambda c: c['population'], reverse=True)[:10]

# Opcional: Usar map para mostrar solo el nombre y la población de forma limpia
print("Top 10 Países más poblados:")
for item in map(lambda c: f"{c['name']}: {c['population']}", top_ten_populated):
    print(item)





