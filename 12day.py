# Day 12 - 30DaysOfPython Challenge
"""
import my_module
print(my_module.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

#import functions from a module
from my_module import generate_full_name, sum_two_nums, person, gravity
#import functions from a module and renaming
from my_module import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g

#os module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

#sys module
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version

#statistics module
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

#math module
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

#string module
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # 
#random module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
"""
#Ejercicios 
#level1
from random import randint
import string
"""def random_user_id():
    caracteres= string.ascii_letters+string.digits
    name=''
    for i in range(6):
        indice=randint(0,len(caracteres)-1)
        name+=caracteres[indice]

    return name
print(random_user_id())

def user_id_gen_by_user():
    n=int(input('Número de caracteres '))
    i=int(input('Número de IDs '))
    caracteres= string.ascii_letters+string.digits
    final=[]
    for e in range(i):
        name=''
        for j in range(n):
            indice=randint(0,len(caracteres)-1)
            name+=caracteres[indice]
        final.append(name)
    return final
print(user_id_gen_by_user())

def rgb_color_gen():
    r=randint(0,255)
    b=randint(0,255)
    g=randint(0,255)
    return r,g,b
print(rgb_color_gen())
"""
#level2
def list_of_hexa_colors(n):
    lista_hex=[]
    caracteres_hex=string.digits +'abcdef'
    for e in range(n):
        color='#'
        for j in range(6):
            indice=randint(0,len(caracteres_hex)-1)
            color+=caracteres_hex[indice]
        lista_hex.append(color)
    return lista_hex
print(list_of_hexa_colors(4 ))

def list_of_rgb_colors(n):
    lista_rgb=[]
    for e in range(n):
        color=[]
        for j in range(3):
            color.append(randint(0,255))
        lista_rgb.append(color)
    return lista_rgb
print(list_of_rgb_colors(4 ))

def generate_colors(color, n):
    if color=="hexa": 
        lista_hex=[]
        caracteres_hex=string.digits +'abcdef'
        for e in range(n):
            color='#'
            for j in range(6):
                indice=randint(0,len(caracteres_hex)-1)
                color+=caracteres_hex[indice]
            lista_hex.append(color)
        return lista_hex
    else:
        lista_rgb=[]
        for e in range(n):
            color=[]
            for j in range(3):
                color.append(randint(0,255))
            lista_rgb.append(color)
        return lista_rgb
print(generate_colors('rgb',4))

#ejercicio3
def shuffle_list(list):
    n = len(list)
    for i in range(len(list)):
        random_index = randint(0, n - 1)
        list[i], list[random_index] = list[random_index], list[i]
    return list
print(shuffle_list(['#Hola','#Soy','#Alex'] ))

