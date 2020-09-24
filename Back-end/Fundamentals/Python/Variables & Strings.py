
# A variable is a container for a value, which can be of various types

''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
''

""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
""

# x = 1           # int
# y = 2.5         # float
# name = 'John'   # str
# is_cool = True  # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic math
a = x + y

# + and -
9 - 2 = 7
9 + 2 + 11

# ** square
3 ** 2 = 9

# / and *
9 / 3 = 3
3 * 3 = 9

# %
10 % 3 = 1

# //
10 // 3 = 3


# Casting
x = str(x)
y = int(y)
z = float(y)


type(z)


# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Printing

  # Concatenate
  print('Hello, my name is ' + name + ' and I am ' + str(age))

  # Arguments by position
  print('My name is {name} and I am {age}'.format(name=name, age=age))

  # F-Strings (python verison 3.6+)
  print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'helloworld'

# Capitalize string
print(s.capitalize())

# Every word start with uppercase letter
print(s.title)

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))
  


# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# Remove backspaces

  # from both sides
  print(s.strip())
  
  # from right side
  print(s.rstrip())
  
  # from left side
  print(s.lstrip())
