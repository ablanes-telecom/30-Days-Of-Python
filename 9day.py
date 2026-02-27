# Day 9 - 30DaysOfPython Challenge
"""
#if condition:
#   this part of code runs for truthy conditions
#elif condition:
#    code
#else:
#   this part of code runs for false conditions

#Short Hand
    #code if condition else code

#ejemplo
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#We can avoid writing nested condition by using logical operator and.
#if condition and condition:
#    code

#If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4: #se tiene que cumplir uno de los dos para ejecutarse
        print('Access granted!')
else:
    print('Access denied!') 

#EJERCICIOS
#level1
age=int(input('Enter your age: '))
if age>=18:
    print('You are old enough to learn to drive.')
else: print('You need',18-age ,'more years to learn to drive.')

my_age=23
if age>my_age:
     if age-my_age==1:
          print('You are 1 year older than me.')
     else: 
          print('You are',age-my_age, 'years older than me.')
elif age==my_age: print('We are the same age.')
else:
     if my_age-age==1:
          print('I am 1 year older than me.')
     else: 
          print('I am',my_age-age, 'years older than me.')

nota=int(input('Tu nota: '))
if nota>=90 and nota<=100:  print('Has sacado un A')
if nota>=80 and nota<=89:  print('Has sacado un B')
if nota>=70 and nota<=79:  print('Has sacado un C')
if nota>=60 and nota<=69:  print('Has sacado un D')
if nota>=0 and nota<=59:  print('Has sacado un F')

mes=input('¿en qué mes estás?')
if mes=='September' or mes=='October' or mes=='November' :
     print('Fall')
elif mes=='June' or mes=='July' or mes=='August': print('Summer')
elif mes=='February' or mes=='January' or mes== 'December': print('Winter')
elif mes=='March' or mes=='April' or mes== 'May':print('Spring')
else: print('No existe payo')

fruits = ['banana', 'orange', 'mango', 'lemon']
apple='apple'
orange='orange'
if apple in fruits: print('That fruit already exist in the list')
else: fruits.append('apple')

if orange in fruits: print('That fruit already exist in the list')
else:  fruits.append('orange') 
print(fruits)
  """
#level3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person: print(person['skills'][int(len(person)/2)])
if 'skills' in person: 
    if 'Python' in person['skills']:print('SI')
else: print('no')

if 'Javascript' and 'React' in person['skills']: print('He is a front end developer')
if person['is_married']==True and person['country']=='Finland': print('{} lives in {}. He is married'.format(person.get('first_name'),person.get('country')))




