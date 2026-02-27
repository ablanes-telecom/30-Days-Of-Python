# Day 5 - 30DaysOfPython Challenge
"""
# syntax
lst = list()
lst = []
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
#Unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

#Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
#negative indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

#Modifying Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
#Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits

#Adding Items to a List
lst = list()
lst.append('item')
lst = ['item1', 'item2']
lst.insert(0, 'item0') ## Inserta el elemento al inicio siempre

#Removing items
lst = ['item1', 'item2']
lst.remove('item1')
#Removing Items Using Pop
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(0) #con el indice
#Removing Items Using Del
lst = ['item1', 'item2']
del lst[0] # only a single item pero también se pueden varios usando los :
del lst        # to delete the list completely

#Clearing
lst = ['item1', 'item2']
lst.clear() #borra la lista

#Copying a List
lst = ['item1', 'item2']
lst_copy = lst.copy()

#Joining Lists
list3 = lst + lst_copy
#using .extend()
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']

#Counting items in a list
lst = ['item1', 'item2']
lst.count('item') #cuenta las veces que hay un item dentro de una lista

#Finding index of an item
lst = ['item1', 'item2']
lst.index('item1') #no hacen falta las comillas en caso de que no sea un string

#Reversing a List
lst = ['item1', 'item2']
lst.reverse()

#Sorting List Items
lst = ['item1', 'item2']
lst.sort()             # ascending
sorted(list)             # sorted(): returns the ordered list without modifying the original list Example:
lst.sort(reverse=True)    # descending
"""
#EJERCICIOS

empty_lst= []
notas_naturales = ['do', 're', 'mi', 'fa', 'sol','sol','si']
print(len(notas_naturales))
last_item= len(notas_naturales)-1
middle_item= int(len(notas_naturales)/2)
nota_grave= notas_naturales[0]
nota_medio = notas_naturales[middle_item]
nota_alta = notas_naturales[last_item]
print('La nota grave es {} la nota del medio es: {}, y la nota mas alta es: {}'.format(nota_grave, nota_medio,nota_alta) )

notas_naturales[5]='la'
notas_naturales.append('re')
notas_naturales.insert(7,'do')
notas_naturales[0].upper()
string=['#;']
union=notas_naturales +string
print(union.index('#;'))
union.sort(reverse=True)
del union[0:4]
del union[-4:]
del union[0:3]
del union
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
junto = front_end + back_end


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print('min {} y max {}'.format(ages[0],ages[-1]))
ages.append(ages[0])
ages.append(ages[-1])
print('la edad media es {}'.format(len(ages)/2))
ages.sort()
print('la max diferencia de edad es {}'.format(int(ages[-1]) - int(ages[0])))

