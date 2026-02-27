# Day 11 - 30DaysOfPython Challenge
"""
#Funcion sin parametros
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name ()

#Funcion devolviendo un valor
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name #podemos devolver cualquier valor
print(generate_full_name())

#Funcion con parametros
def greetings (name): # se pueden incluir varios parametros separados por la coma
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Asabeneh'))

#Pasango argumentos con Key y Value
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh') # de esta forma da igual el orden porque van con la variable

#default parameters
def greetings (name = 'Peter'): # en caso de no recibir ningun input usará 'peter'.
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

#Aribitrary number: cuando no sabemos cuantas cosas le vamos a meter como inputs, pnemos un *delante, 
# se pueden combinar con otros con una ,
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

#Dictionary unpacking
# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York

#Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 9

#EJERCICIOS
#nivel1
def suma(a,b):
    return a+b
print(suma(2,2))

def area_c(r):
    return (r**2)*2
print(area_c(3))

def add_all_nums (*num):
    total=0
    for n in num:
        total+=n
    return total

print(add_all_nums(2,2,2,2,3))

def convert_celsius_to_fahrenheit(C):
    return C * 9/5 + 32
print(convert_celsius_to_fahrenheit(30))

def check_season(m):
    estacion=''
    if m =='January' or m=='December' or m=='February': return  'Winter'
    elif m =='May' or m=='April' or m=='March': return  'Spring'
    elif m =='September' or m=='October' or m=='November': return  'Autum'
    elif m =='July' or m=='June' or m=='August': return  'Summer'
    else: return 'no válido'

print(check_season('January'))

import math
def solve_quadratic_eqn(x):
    a=2
    b=3
    c=5
    return a*(x**2)+b*x+c
print(solve_quadratic_eqn(1))

def print_list(list):
    for i in list:
         print(i)
    return 'check'

    
print(print_list(['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'},False]))

def reverse_list(array):
     reversed=[]
     for i in array:
          reversed.insert(0,i)
     return reversed
print(reverse_list([1, 2, 3, 4, 5]))

def capitalize_list_items(list):
    capitalizado=[]
    for i in list:
        capitalizado.append(i.capitalize())
    return capitalizado
print(capitalize_list_items(['hola','alex']))

def add_item(list,extra):
   list.append(extra)
   return list
print(add_item([5,5,5],6))

def remove_item(list,extra):
   list.remove(extra)
   return list
print(remove_item([5,5,5],5))
        
def sum_of_numbers(x):
    suma=0
    for i in range(0,x+1):
        suma+=i
    return suma
print(sum_of_numbers(10))

def sum_of_odds(x):
    suma=0
    for i in range(0,x+1,2):
        suma+=i
    return suma
print(sum_of_odds(100))

#level2
def evens_and_odds(int):
    pares=[]
    impares=[]
    if int<0: return 'numero no válido'
    else: 
        for i in range(0,int+1,2):
            pares.append(i)

        for j in range(1,int+1,2):
            impares.append(j)
    return len(pares),len(impares)
print(evens_and_odds(100))

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
print(factorial(5))

def is_empty(d):
    if len(d)==0: return True
    else: return False
    
print(is_empty('hola'))


def media(list):
    suma=0
    valores=len(list)
    for i in list:
        suma +=i
    return suma/valores
print(media([1,2,3,4,5,6,7,8,9,10]))

def greet(nombre='Guest'):
    print('Hi',nombre) 
print(greet())

def show_args(**args):
    for n, v in args.items():
        print(n,v)
show_args(name="Alice", age=30, city="New York")

#level3
def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2,n):
        if n%i==0: return False
    return True
print(is_prime(8))
print(is_prime(7))

def unico(list):
    return len(list)==len(set(list))

print(unico([3,4,5,6,6]))
def unico(list):
    tipos=set()
    for i in list:
        tipos.add(type(i))
    return len(tipos)==1

print(unico([3,4,5,6,6]))

def is_valid_variable(name):
    # .isidentifier() es un método que ya viene con los textos en Python
    # Comprueba casi todas las reglas (letras, números, guiones bajos)
    return name.isidentifier()
print(is_valid_variable("mi_variable"))"""


from countries_data import countries

def most_spoken_languages(countries):
    paises_ordenados = sorted(countries, key=lambda x: x['population'], reverse=True)
    top_10_limpio = [{'country': p['name'], 'population': p['population']} for p in paises_ordenados[:10]]
    return top_10_limpio
print(most_spoken_languages(countries))





          
          
