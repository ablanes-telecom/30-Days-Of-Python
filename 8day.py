# Day 8 - 30DaysOfPython Challenge

#creating a dictionary
empty_dict = {}
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
#The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.
len(person)
person['first_name']#usando el comando get hacemos que en caso de no existir la clave no devuelve error

#Adding Items to a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

#Modifying Items in a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

#Checking Keys in a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
'key2' in dct # True
'key5' in dct # False

#Removing Key and Value Pairs from a Dictionary
dct.pop('key1') # removes key1 item
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

#Changing Dictionary to a List of Items
dct.items() # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#Clearing a Dictionary
dct.clear() # None

#Deleting a Dictionary
del dct

#Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

#Getting Dictionary Keys as a List
keys = dct.keys()  # dict_keys(['key1', 'key2', 'key3', 'key4']) 

#Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()   # dict_values(['value1', 'value2', 'value3', 'value4'])

#EJERCICIOS
dog ={}
dog['name'] = 'valdi'
dog['breed']='mezcla'
dog['año']='5'
dog['skills']=['saltar','correr', 'dar la patita']
#dog = {'name': 'valdi', 'breed': 'mezcla', 'año': '5'}
print(len(dog))
print(type(dog['skills']))
dog['skills'].append('sentarse')
keys_list=list(dog.keys())
values_list=list(dog.values())
print(keys_list)
print(values_list)
dictionary_conv=dog.items()
tuple=tuple(dictionary_conv)
print(tuple)
dog.pop('skills')
del dog



