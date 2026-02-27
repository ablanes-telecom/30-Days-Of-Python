# Day 3 - 30DaysOfPython Challenge

# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False) 

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False """

#Ejercicio 1:
age=23
height=1.90
Complex =3-1j
base=input ('Base: ')
altura=input('Altura: ')
print('El aerea del triángulo es:', float(base) * float(altura) / 2 )
print('El area del rectangulo es:', float(base) * float(altura))
#calcular el perímetro de un triángulo
side_a = input('a: ')
side_b = input('b: ')
side_c = input('c: ')
print('El perímetro del triángulo es:', float(side_a) + float(side_b) + float(side_c))

radius=input('Introduce el radio del círculo: ')
print('Area=', 3.14*(float(radius)**2))
print('Circunferencia=' ,2*3.14*float(radius))
slope_1 = 2
slope_2 = (10-6)/(2-1)
print(slope_1>slope_2)
x=1
print('y=', (x**2) + 6*x + 9)
print('El valor de x que hace que y=0 es:', -3 )

print(len('Python')!=len('Dragon'))
print('on' in 'Python' and 'on' in 'Dragon')
print('on' is not 'Python' and 'on' is not 'Dragon')
print(str(float(len('python'))))

#Comprobar que un numero es par
print('Si el resultado es 0 es par=',5%2)
print(7/3==int(2.7))
print('10'==10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours=40
cobro_hora=28
print('Tu cobre semanal es:' , hours*cobro_hora)
