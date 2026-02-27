# Day 2 - 30DaysOfPython Challenge

print(len('Thirty'))        # length of a string, len() is a built-in function
print (int(23.2))        # converting float to int, int() is a built-in function
print (float(23))        # converting int to float, float() is a built-in
"""input('What is your name? ') # input() is a built-in function to get user inputAl"""

help('keywords')

max(2, 3, 4)             # max() is a built-in function to find the maximum of given numbers
min(2, 3, 4)             # min() is a built-in function
sum([2, 3, 4])          # sum() is a built-in function to find the sum of given numbers

# Variables in Python
first_name = 'Alex'
last_name = 'Blanes'
country = 'Spain'
city = 'Valencia'
age = 23
is_married = False
skills = ['Guitarra', 'Python']
person_info = {
   'firstname':'Alex',
   'lastname':'Blanes',
   'country':'Spain',
   'city':'Valencia'
   }
print('Person information: ', person_info)
print(type(person_info))
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True # multiple variable assignment in one line

#inputs
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

#EJERCICIO 1 y 2
nombre= 'Alex' 
apellido= 'Blanes'
nombre_completo= nombre + apellido
martina_guapa = True 
guitarras, panyuelos, libretas = 2, 2, 4
print(type(guitarras))
num_one = 5
num_two = 4
suma= num_one + num_two
diff= num_one - num_two
product= num_one * num_two
reminder= num_one % num_two
floor_division= num_one // num_two
#Calcular area de un circulo de 30 m
radio= input('Introduce el radio del circulo: ')
area= 3.1415 * (float(radio)**2)
print(area)

nombre= input('Nombre:')
apellido= input('Apellido:')
edad= input('Edad:')
informacion=(nombre, apellido, edad)
print (informacion[0])

