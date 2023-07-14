# СПИСКИ. ЕГО ЗНАЧЕНИЯ ИЗМЕНЯЕМЫЕ, МЫ МОЖЕМ ЕГО ИНДЕКСИРОВАТЬ, ЗНАЧЕНИЯ НЕУНИКАЛЬНЫ СОЗДАЕТСЯ [] ИЛИ ФУНКЦИЕЙ LIST
list_1 = [] #creat empty list
list_1 = list() #creat empty list with function
list_1 = [1, 2, 3, 8] # creat not empty list

print(*list_1) #print without []
print(list_1) #print like array

for i in list_1:
    print(i) #sequential printing
    
print(len(list_1)) #print a lenght of list

print(list_1[1]) #print element with index in []

list_1 = [1, 5]
print(list_1)
list_1.append(8) #add element in the end
print(list_1)
list_1.append(85)
print(list_1)

list_1 = [] #create new list
print(list_1) 
for i in range(5): #make a list from 5
    list_1.append(i) #add next number in list
    print(list_1) 


#deleting last element
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) #delete and return last element in list 
print(list_1)
print(list_1.pop(0)) #delete and return element with index in ()
 

#add element on position
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11)) #first arg its position, second arg is value which need to set

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])                          # 1
print(list_1 [-1])                        # 10
print(list_1[-5])                         # 6
print(list_1[:])                          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])                         # [1, 2]
print(list_1[5:])                         # [6, 7, 8, 9, 10]
print(list_1[len(list_1)-2:])             # [9, 10]
print(list_1[2:9])                        # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])                      # []
print(list_1[0:len(list_1):6])            # [1, 7]
print(list_1[::6])                        # [1, 7]

#КОРТЕЖ - неизменяемый список. КОРТЕЖ ИНДЕСИРУЕТСЯ, ЕГО ЭЛЕМЕНТЫ НЕ ВЯЛЮТСЯ УНИКАЛЬНЫМИ, СОЗДАЕТСЯ () ИЛИ tuple
t = []
print(type[t]) #make new cortej

t = (1, ) #add ann allement in cortaj
print(type[t])

v = [1, 8, 9] #creat new list
print(v)
print(type(v)) #print type of v

v = tuple(v) #change list like cortaj
print(v)
print(type(v))

a = 1
b = 2
#or

a, b = 1, 2

# or

a = b = 1

a, b, c = v

print(a, b, c) #unpacking cortaj

t = (1, 2, 3, 5, )

for i in t:
    print(i)
    
for i in range(len(t)):
    print(t[i])
    
#СЛОВАРИ - неупорядоченные коллекции произвольныз объектов с поиском по ключу. СЛОВАРИ ИЗМЕНЯЕМЫ ЧАСТИЧНО: МОЖНО ИЗМЕНЯТЬ ЭЛЕМЕНТЫ И ЗНАЧЕНИЯ, КЛЮЧИ ИЗМЕНЯТЬ НЕЛЬЗЯ, ОН НЕ ИНДЕКСИРУЕТСЯ И УНИКАЛЕН ОН ТОЖЕ ЧАСТИЧНО, УНИКАЛЬНЫ ЭЛЕМЕНТЫ И КЛЮЧИ, ЗНАЧЕНИЯ В СЛОВАРЯХ - НЕУНИКАЛЬНЫ, СОЗДАЕТСЯ С ПОМОЩЬЮ {}, {KEY: VALUE} ИЛИ DICT()

d = {} #creat new vocabulary
d = dict() #creat new vocabulary

d['q'] = 'qwerty' #add an element with key 'q'
print(d) # print full record q: qwerty

d['w'] = 'werty' #add an element with key 'w'
print(d['q']) # print element

dictionary = {}
dictionary = {'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'}
print(dictionary) #{'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'} 
print(dictionary['up']) #u

#the type of key can be different

dictionary['left'] = 'h' #change the ellement with key ['...']
print(dictionary['left']) #h

print(dictionary['type']) #KeyError: 'type'

del dictionary['left'] #delete an ellement

for item in dictionary:
    print(item) #print the keys by new string
    print('{}:{}'.format(item, dictionary[item])) #print ellements with keys by new strings
    
    for (k,v) in dictionary.items():
        print(k,v)
        
print(dictionary.items()) #print vocabulary in which each element it's cortaj 

#МНОЖЕСТВА. ЯВЛЯЮТСЯ ИЗМЕНЯЕМЫМ ОБЪЕКТОМ, ЕГО ПОСЛЕДОВАТЕЛЬНОСТЬ НЕИНДЕКСИРУЕТСЯ, содержат в себе уникальные значения,  ВЫЗЫВАЕТСЯ ЛИБО {ELEMENT, ELEMENT} ЛИБО SET()
colors = set() #creat an empty set
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}

colors.add('grey') #add an element on set 
print(colors) # {'red', 'green', 'blue', 'grey'}

colors.add('red') #if you wanna add an exist element on set - u can't to do it
print(colors)

colors.remove('red') #delete an element
colors.remove('red') #if you try to delete element which not exist in set - u will see an error #KeyError
colors.discard('red') #checking and delete element in set
colors.clear() #empty set 
print(colors)

a = {1, 2, 3, 5, 8}                             
b = {2, 5, 8, 13, 21}
c = a.copy()                                    # copy set in c {1, 2, 3, 5, 8}     
u = a.union(b)                                  # set 'u' will be contain unique value by set 'a' and 'b' {1, 2, 3, 5, 8, 13, 21} 
i = a.intersection(b)                           # find an element in two sets which have an both sets {8, 2, 5}
d1 = a.difference(b)                            # math operation of different: set'a' - set'b' = {1, 3}
dr = b.difference(a)                            # math operation of different: set'b' - set'a' = {13, 21}
q = a.union(b).difference(a.intersection(b))    #firstly we find 'intersection', after - cointain a and b and last - we make a math operation of different: union set - intersection set = {1, 21, 3, 13}

a = {1, 8, 6}

b = frozenset(a) #notchanging set, frozen set -- НЕИЗМЕНЯЕМЫЕ МНОЖЕСТВА

# СТРОКА. НЕИЗМЕНЯЕМА, ПОД НОВЫЕ СОЗДАЮТСЯ НОВЫЕ ПЕРЕМЕННЫЕ, ЕЕ МОЖНО ИНДЕКСИРОВАТЬ, ЕЕ ЗНАЧЕНИЯ НЕ ДОЛЖНЫ БЫТЬ УНИКАЛЬНЫ, СОЗДАЁТСЯ ЛИБО '' ИЛИ ""

#LIST COMPREHENSION - ГЕНЕРАЦИЯ СПИСКОВ
list_1 = [i for i in range(1, 101)] #создать список чисел от 1 до 100
#эту функцию мы записывали ранее как:
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)

#создать список чисел от 1 до 100 только из четных чисел
list_1 = [i for i in range(1, 101) if i % 2 == 0]

#well, let's try a creat an cortage with each number and with that method you can use any action
list_1 = [(i, i) for i in range (1, 100)]

# TYPES OF ERROR
## SyntaxError
number_first = 5
number_second = 7
if number_first > number_second #!!!!
    print(number_first)
    
# indentationTrror
number_first = 5
number_second = 7
if number_first > number_second 
print(number_first) #!!!!

#TypeError
text = 'Python'
number = 5
print(text + number) #!!!!

#ZeroDivision
number_first = 5
number_second = 0
print(number_first // number_second) #!!!!

#KeyError
dictionary = {i:  'Monday', 2: 'Tuesday'}
print(dictionary[3]) #!!!!

#NameError
name  = "Ivan"
print(names)  #!!!!

#ValueError
text = 'Python'
number = 
print(int(text)) #!!!!

