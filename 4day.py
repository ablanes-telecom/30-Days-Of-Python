# Day 4 - 30DaysOfPython Challenge
#STRINGS
"""
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
#Escape sequences
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

#String formatting (python3)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
#String interpolation (pytnon3.6)
a=4
b=3
print(f'{a}+{b}= {a+b}')

#Unpacking Characters

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
#Accessing Characters in Strings by Index
first_letter = language[0]
print(first_letter) # P
last_letter = language[-1]
print(last_letter) # n

#Slicing Python Strings
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

#Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

#Skipping Characters While Slicing
pto = language[0:6:2] #
print(pto) # Pto

#Metodos String
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

prueba = 'thirty days of python'
print(prueba.isalnum()) # False, space is not an alphanumeric character
print(prueba.isalpha()) # True, checkea si todo el argumento contiene de la A a la z.
print(prueba.isdecimal())  # False
numero='123'
print(numero.isdigit())   # True
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

# la diferencia entre index y find radica en el error y que el index tb sirve para listas
"""
#EJERCICIOS
uno='Thirty'
dos='Days'
tres='Of'
cuatro='Python'
print('{} {} {} {}'.format(uno,dos,tres,cuatro))

company="Coding For All"
print('len()',len(company),'.upper()',company.upper(),'.lower()',company.lower(), '.capitalize()',company.capitalize(), '.title()',company.title(), '.swapcase()',company.swapcase())
print('eliminar la primera palabra', company[7:])
print(company.index('Coding'))
print(company.replace('Coding','Python'))
print(company.split(' '))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print(company[-1])
name='Python For Everyone'
print('siglas', name[0]+name[7]+name[11])
print(name.index('P'))
print(name.rfind('o'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.replace(' because because because ',' '))
sentence = 'You cannot end a sentence with because because because is a conjunction'

# Buscamos dónde empieza la frase
start = sentence.find('because because because')
# Calculamos dónde termina sumando la longitud de la frase
end = start + len('because because because')

# Aplicamos el slicing [inicio:fin]
phrase = sentence[start:end]

print(phrase)

substring= 'Coding'
print(substring.startswith('C'))
print('   Coding For All      '.strip())
list=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(list))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
