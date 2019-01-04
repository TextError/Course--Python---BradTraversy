# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
  
  def has_birthday(self):
    self.age += 1

class Costumer(User):
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.ballance = 0
  
  def set_ballance(self, ballance):
    self.ballance = ballance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and I owe a ballance of {self.ballance}'


# Init user Obj
brad = User('Brad Traversy', 'brad@test.com', 37)
janet = User('Janet Williams', 'janet@test.com', 27)

# Edit property
brad.age = 38
janet.has_birthday()

print(brad.name)
# Call method
print(janet.greeting())

# Init customer
john = Costumer('John Doe', 'John@test.com', 40)
john.set_ballance(500)

print(john.name)
print(john.greeting())