# Day 18 - 30DaysOfPython Challenge
#regular expressions: sirven para encontrar patrones en data
import re
"""
#match:re.match(substring, string, re.I) --> returns an object only if the text starts with the pattern.
txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0 15
substring = txt[start:end]
print(substring)       # I love to teach

#Search: re.search(substring, string, re.I) -->Search returns a match object with a first match that was found, otherwise it returns None
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

#Findall: 
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
#si no tenemos re.I activada tendremos que poner todos los casos (min y mayusculas):
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

#Replacing a Substring
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend Javascript for a first programming language
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend Javascript for a first programming language
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
matches = re.sub('%', '', txt)
print(matches)

#Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol

#Writing RegEx Patterns
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']
# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
#Square bracket
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']

#Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
#One or more times(+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

#Period(.)
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']
regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

#Zero or more times(*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

#Zero or one time(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

#Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] 

#Cart
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
"""
#EJERCICIOS
#level1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
palabras=re.findall(r'\w+',paragraph,re.I)
conteo=[]
palabras_vistas=[]
for i in palabras:
    if i not in palabras_vistas:
        conteo.append((len(re.findall(r'\b' + i + r'\b',paragraph)),i))
        palabras_vistas.append(i)

conteo.sort(reverse=True)
print(conteo)

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
str_points=str(points)
numeros=re.findall(r'-?\d+',str_points)
valormin=numeros[0]
valormax=numeros[0]
for i in numeros:
    if int(i)>int(valormax):valormax=i
    if int(i)<int(valormin):valormin=i
print(int(valormax)-int(valormin))

#level2
def is_valid_variable(string):
    # El patrón verifica que empiece por letra/guion bajo y siga con letra/número/guion bajo
    pattern = r'^[a-z_][a-z0-9_]*$'
    # Usamos re.I para que no importe mayúsculas/minúsculas
    if re.match(pattern, string, re.I):
        return True
    else:
        return False

# Pruebas
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False (contiene guion medio)
print(is_valid_variable('1first_name')) # False (empieza por número)
print(is_valid_variable('firstname'))   # True

#level3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(string):
    return re.sub(r'[^a-z0-9A-Z ?!.]','',string)
def most_frequent_words(string):
    palabras=re.findall(r'\w+',string,re.I)
    conteo=[]
    palabras_vistas=[]
    for i in palabras:
        if i not in palabras_vistas:
            conteo.append((len(re.findall(r'\b' + i + r'\b',string)),i))
            palabras_vistas.append(i)
    conteo.sort(reverse=True)
    return conteo[:3]
cleaned_text=clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))