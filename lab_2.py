"""
Laboratory job #2. Data types
"""
# Data types
#
# #String
# # 1.
# string1 = 'This is a string.     '
# string2 = '     This is another string.'
# # 2.
# print('Concatenation: ' + string1 + ' ' + string2)
# # 3.
# print('String1 length: ', len(string1))
# print('lower(): ' + string2.lower())
# print('title(): ' + string2.title())
# print('upper(): ' + string1.upper())
# print('rstrip(): ' + string1.rstrip())
# print('lstrip(): ' + string2.lstrip())
# print('strip()' + string1.strip())
# print('strip("0")' + string2.strip('T, g.'))
#
# # 4.
# d = 'qwertyuiop[]'
#
# ch = d[3]
# print(d[5] + ' ' + ch)
# # 5. Slicing
# chm = d[1 : 3]
# print(chm)
# # 6.
# print(d[1:])
# print(d[:3])
# print(d[:])
# print(d[1:5:2])
# # 7.
# # d[2] = 'o'    TypeError: 'str' object does not support item assignment
#
# # Numeric
# # 1.
# a = 152
# b = 43
# # 2.
# print(a/b)
# print(a//b)
# print(b/a)
# print(a%b)
# print(b**a)
#
# # 3.
# # param = 'string' + 123    TypeError: can only concatenate str (not "int") to str
# param = 'string' + str(123)
# print(param)
#
# # Data conversion
#
# # 1.
# param = 'string' + str(123)
# print(param)
#
# # 2.
# n1 = input('Enter a number: ')
# n2 = input('Enter another number: ')
# n3 = float(n1) + float(n2)
# print(n1 + ' plus ' + n2 + ' = ', n3)
#
# # String format
# # 1. https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method
#
# # 2.
# a = 1/3
# print("{:7.3f}".format(a))
#
# # 3.
# a = 2/3
# b = 2/9
# print("{:7.3f} {:7.3f}".format(a, b))
# print("{:10.3e} {:10.3e}".format(a, b))
#
# # 4.
# print(n1 + ' plus ' + n2 + ' = ', '{:10.3f}'.format(n3))

# Lists

# list1 = [43, 4, 949, 54, 93, 0, 121, 584, 3562]
# print(dir(list))

# help(list1)
#
# help(list.insert)
# help(list.append)
# help(list.sort)
# help(list.remove)
# help(list.reverse)

# list1.insert(1, 33)
# list1.append(555)
# list1.sort()
# list1.remove(3562)
# print(list1)
# list1.reverse()
# print(list1)
# list1.pop(list1.index(0))	# removes an element at specified position
# print(list1)
# list1.pop(-1)	# remove last element
# print(list1)

# Sorting

# fruits = ['banana', 'orange', 'mango', 'apple']
# fruits.sort(reverse=True)
# print(fruits)
#
# list2 = [3,5,6,2,33,6,11]
# lis = sorted(list2)
# print(list2, lis)

# Tuples

# print(dir(tuple))
# help(tuple.count)
# help(tuple.index)

# seq = (2,8,23,97,92,44,17,39,11,12,44)
# print(seq.index(92))
# print(seq.count(44))
# listseq = list(seq)
# print(type(listseq))

# Dictionary

# D = {"food": "Apple", "quantity": 4, "color": "Red"}
# print(D["food"])
# D["quantity"] += 6
# print(D["quantity"])

# dp = {}
# dp['name'] = input('Enter name: ')
# dp['age'] = input('Enter age: ')
# print(dp)

# Nested Data Storage

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
	   'job': ['dev', 'mgr'],
	   'age': 25}
print('The full name is', rec['name']['firstname'],
	  rec['name']['lastname'])
print('The first name is', rec['name'].get('firstname'))
print('Job list:', ', '.join(rec.get('job')))
rec['job'].append('janitor')
print('Job list after append:', ', '.join(rec.get('job')))
print('Person info')
print('Name:', rec['name']['firstname'], rec['name']['lastname'])
print('Job:', ', '.join(rec.get('job')))
print('Age:', rec.get('age'))
