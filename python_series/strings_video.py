#!/usr/bin/env python3

print("This is string")
print('This is another string')

x = 5
y = 10

# C String formatting
print('This is a string with a variable %d' % x)

# format()
print('This is another string with a variable {0} and {1}'.format(x, y))

# f-string
print(f'This is a string with variable {x} and  {y}')

x = 'This is the beginning of the string'
y = 'This is the end of the string'

print(x + y)
print(x, y)

x = 'This string'
print(x * 5)

# Comparison
a = 'Aaaaa'
b = 'Bbbbbb'
print(a < b)


# iteration 
for c in x:
	print(c)