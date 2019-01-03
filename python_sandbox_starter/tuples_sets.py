# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
# Create tuple using contructor
# fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))
print(fruit_tuple)

# Get sigle value
print(fruit_tuple[1])

# Can not change value
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have traling comma
fruit_tuple_2 = ('Apple',)

# Get Length of tuple
print(len(fruit_tuple_2))

# Delete all tuple
del fruit_tuple_2


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mongo'}
fruit_set = {'Apple', 'Orange', 'Mongo', 'Apple'} #No duplicate members
print(fruit_set)

# Check if in set
print('Apple' in fruit_set)

# Add to set
fruit_set.add('Grape')
print(fruit_set)

# Remove from set
fruit_set.remove('Grape')
print(fruit_set)

# Clear set
fruit_set.clear()
print(fruit_set)

# Delete set
del fruit_set