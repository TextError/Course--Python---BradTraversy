# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

# Using a contructor
# person = dict(first_name= 'John', last_name= 'Doe', age= 30)

print(person)

# Access single value
print(person['first_name'])
print(person.get('last_name'))

# Add key value
person['phone'] = '555-555-555'
print(person)

# Get keys
print(person.keys())

# Get items
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')
print(person)

# Get length
print(len(person))

# Clear
person.clear()
print(person)

# List of dict
people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Bob', 'age': 20}
]

print(people)

# Get value
print(people[1]['name'])