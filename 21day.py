# Day 21 - 30DaysOfPython Challenge

""" Python is an object oriented programming language. Everything in Python is an object, 
with its properties and methods. A number, string, list, dictionary, tuple, set etc. used 
in a program is an object of a corresponding built-in class. We create class to create an object.
A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class 
to create an object. The class defines attributes and the behavior of the object, while the object,
 on the other hand, represents the class. """
"""
#Creating a Class
 class ClassName:
         code goes here 
class Person:
  pass
print(Person)
#We create an object by callling a class
p = Person()
print(p)

#Class constructor
class Person:
      def __init__ (self, name): #The init constructor function has self parameter which is a reference to the current instance of the class Examples
        # self allows to attach parameter to the class
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)

#podemos añadir más parametros a la funcion: 
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

#Object methods
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())

#Object Default Methods
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

#Method to Modify Class Default Values
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

#Inheritance
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
#When we add the init() function, the child class will no longer inherit the parent's init() function.

#Overriding parent method
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
"""
#EJERCICIOS
#level1
class data():
    
    def count(nums):
        return len(nums)
    def sum(nums):
        res=0
        for i in nums:
            res+=i
        return res
    def min(nums):
        min=nums[0]
        for i in nums:
            if i<=min: min=i
        return min
    def max(nums):
        max=nums[0]
        for i in nums:
            if i>=max: max=i
        return max
    def range(nums):
        max=nums[0]
        min=nums[0]
        for i in nums:
            if i>=max: max=i
            elif i<min: min=i
        return max-min
    def mean(nums):
        suma=0
        for i in nums:
            suma+=i
        return suma/len(nums)
    def median(nums):
        return int(len(nums)/2)
    def mode(nums):
        dict={}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        max_valor = max(dict.values())
        resultado = {}
        for numero, repeticiones in dict.items():
            if repeticiones == max_valor:
                resultado[numero] = repeticiones
        return resultado
    def std(nums):
        n = len(nums)
        media = sum(nums) / n
        
        # Paso 2 y 3: Restar y elevar al cuadrado
        suma_cuadrados = 0
        for i in nums:
            suma_cuadrados += (i - media)**2
        
        # Paso 4 y 5: Promedio y Raíz (usando exponente 0.5)
        varianza = suma_cuadrados / n
        return varianza**0.5
    def fd(nums):
        total_datos = len(nums)
        conteo = {}
        
        # 1. Obtenemos la frecuencia absoluta (lo que ya sabes hacer)
        for i in nums:
            conteo[i] = conteo.get(i, 0) + 1
        
        # 2. Vamos a crear un diccionario más detallado
        tabla = {}
        for num, veces in conteo.items():
            porcentaje = (veces / total_datos) * 100
            tabla[num] = {
                "abs": veces,
                "rel": f"{porcentaje}%"
            }
        
        return tabla
    def describe(nums):
        return {
            "count": data.count(nums),
            "sum": data.sum(nums),
            "min": data.min(nums),
            "max": data.max(nums),
            "range": data.range(nums),
            "mean": data.mean(nums),
            "median": data.median(nums),
            "mode": data.mode(nums),
            "std": data.std(nums),
            "fd": data.fd(nums)
        }
        


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
print(data.count(ages))
print(data.sum(ages))
print(data.min(ages))
print(data.max(ages))
print(data.range(ages))
print(data.mean(ages))
print(data.median(ages))
print(data.mode(ages))
print(data.std(ages))
print(data.fd(ages))

print(data.describe(ages))

#level2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # Los iniciamos vacíos para ir agregando con los métodos
        self.incomes = []  # Ejemplo: [{"amount": 1000, "description": "Salary"}]
        self.expenses = [] # Ejemplo: [{"amount": 200, "description": "Rent"}]

    def add_income(self, amount, description):
        self.incomes.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        # Sumamos solo el valor 'amount' de cada diccionario en la lista
        return sum(item['amount'] for item in self.incomes)

    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)

    def account_balance(self):
        # El balance es ingresos menos gastos
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"{self.firstname} {self.lastname} tiene un balance de: {self.account_balance()}"

persona = PersonAccount("Ana", "García")
persona.add_income(2500, "Salario")
persona.add_expense(800, "Alquiler")
persona.add_expense(150, "Internet")

print(persona.account_info()) # Ana García tiene un balance de: 1550
print(f"Total ingresos: {persona.total_income()}")
    