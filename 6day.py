# Day 6 - 30DaysOfPython Challenge

#Creating tuples
empty_tuple = ()
empty_tuple = tuple()
#len(empty_tuple())
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
all_items = fruits[0:]         # all items
middle_two_items = fruits[1:3]  # does not include item at index 3
all_items =fruits[-4:]         # all items
middle_two_items = fruits[-3:-1]  # does not include item at index 3 (-1)

#Changing Tuples to Lists
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

#Checking an Item in a Tuple
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

#Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

#Deleting Tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1

#EJERCICIOS
tpl=()
tpl=('Alex', 'Emma')
tpl2=('Montse','David')
familia= tpl+tpl2
print(len(familia))
print('Hijos {} y {} y padres {} {}'.format(familia[0],familia[1],familia[2],familia[3]))
hijos=familia[:2]
print('Hijos {}'.format(hijos))
del hijos

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Denmark' in nordic_countries)






