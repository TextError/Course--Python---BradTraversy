# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create func
def sayHello():
  '''
  Prints Hello
  '''
  print('Hello')

sayHello()

def sayHelloArg(name = 'Beth'):
  '''
  Prints Hello + name if exists
  '''
  print('Hello ' + name)

sayHelloArg('Sam')

sayHelloArg()

# Return Value
def getSum(num1, num2):
  total = num1 + num2
  return total

numSum = getSum(4,5)
print(numSum)

def addOneToNum(num):
  num += 1
  return num

num = addOneToNum(5)
print(num)



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(3,4))

addOneToNum = lambda num : num + 1
print(addOneToNum(3))