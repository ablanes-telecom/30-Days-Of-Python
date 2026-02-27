# Day 7 - 30DaysOfPython Challenge

#Creating a Set
st = set()
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
'item' in st  # True

#Adding and removing Items to a Set
st.add('item5')
st.update(['item5','item6','item7']) #The update() allows to add multiple items to a set
st.remove('item7')
st.pop()  # removes a random item from the set and returns it

#Clearing items in a set
st.clear()

#Deleting a Set
del st

#Converting list to a set
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

#Joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
st1.update(st2) #This method inserts a set into a given set

#Finding Intersection Items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2

#Checking Subset and Super Set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

#Checking the Difference Between Two Sets: devuelve A-B (los que estan en A pero no en B)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

#Finding Symmetric Difference Between Two Sets
#Este comando devuelve los elementos que están en uno de los conjuntos o en el otro, 
#pero no en ambos (es decir, excluye la intersección).
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

#Joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

#EJERCICIOS
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Sony', 'Analog Devices'])
it_companies.remove('IBM')
#la diferencia entre remove() y discard() esque remove si no está ol objeto devuelve un error
A.update(B)
print(A)
print(A.isdisjoint(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.symmetric_difference(B) )
del A,B

age = [22, 19, 24, 25, 26, 24, 25, 24]
set_age=set(age)
#string es cualquier objeto que contiene una secuencia inmutables de caracteres
#una lista es un conjunto de objetos mutable y ordenado y permite duplicados
#un set es un conjunto de objetos mutable (pero no los elementos dentro de él), desordenado y no permite duplicados
#un tuple es un conjunto de objetos inalterable y ordenado
frase= 'I am a teacher and I love to inspire and teach people'
frase_set= set(frase)
print('Letras únicas ya que en un set no se pueden tener duplicados:',len(frase_set),'los caracteres son: ',frase_set)






