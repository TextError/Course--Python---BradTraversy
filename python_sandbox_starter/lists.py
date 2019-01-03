# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1,2,3,4,5]
# Create List using contructor
numbers = list((1,2,3,4,5))
fruits = ['Apple', 'Oranges', 'Grapes', 'Pears']

print(type(numbers))
print(numbers)

# Get value
print(fruits[1])

# Get length
print(len(fruits))

# Append to List
fruits.append('Mangos')
print(fruits)

# Remove from List
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from position
fruits.pop(3)
print(fruits)

# Revers List
fruits.reverse()
print(fruits)

# Sort the List
fruits.sort()
print(fruits)

# Revers sort List
fruits.sort(reverse=True)
print(fruits)