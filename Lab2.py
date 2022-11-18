# Laboratory job #2.
# Data types

#String
# 1.
string1 = 'This is a string.     '
string2 = '     This is another string.'
# 2.
print('Concatenation: ' + string1 + ' ' + string2)
# 3.
print('String1 length: ', len(string1))
print('lower(): ' + string2.lower())
print('title(): ' + string2.title())
print('upper(): ' + string1.upper())
print('rstrip(): ' + string1.rstrip())
print('lstrip(): ' + string2.lstrip())
print('strip()' + string1.strip())
print('strip("0")' + string2.strip('T, g.'))

# 4.
d = 'qwertyuiop[]'

ch = d[3]
print(d[5] + ' ' + ch)
# 5. Slicing
chm = d[1 : 3]
print(chm)
# 6.
print(d[1:])
print(d[:3])
print(d[:])
print(d[1:5:2])
# 7.
# d[2] = 'o'    TypeError: 'str' object does not support item assignment

# Numeric
# 1.
a = 152
b = 43
# 2.
print(a/b)
print(a//b)
print(b/a)
print(a%b)
print(b**a)

# 3.
# param = 'string' + 123    TypeError: can only concatenate str (not "int") to str
param = 'string' + str(123)
print(param)

# Data conversion

# 1.
param = 'string' + str(123)
print(param)

# 2.
n1 = input('Enter a number: ')
n2 = input('Enter another number: ')
n3 = float(n1) + float(n2)
print(n1 + ' plus ' + n2 + ' = ', n3)

# String format
# 1. https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method

# 2.
a = 1/3
print("{:7.3f}".format(a))

# 3.
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

# 4.
print(n1 + ' plus ' + n2 + ' = ', '{:10.3f}'.format(n3))

# Lists

