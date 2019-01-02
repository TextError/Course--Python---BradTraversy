# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x = 1             # int
y = 2.15          # float
name = 'Brad'     # string
is_cool = True    # bool


# Multiple assigment #
x, y , name, isCool = (1, 2.15, 'Brad', True)
# print(x, y, name, isCool)


# Basic Math #
a = x + y
# print(a)


# Check type # 
print(type(a))


# Casting # 
x = str(x)
y = int(y)
z = float(y)

print(type(x))