# Local scope::::::
def greet():
  message='Hello python'
  print(message)

# greet()

# Enclosing scope::::
# A function defined inside another function then the variable defined in outer function can be accessible to the inner function......

def outer():
  msgOuter = 'Belong to outer function'
  a=100
  def inner():
    msgInner = "this belongs to inner function"
    nonlocal a
    a=200
    print(msgInner)
    print(a)
    print('##############################')
    print(msgOuter)

  inner()
  print(a)

# outer()

# Global variable:: a variable created at toplevel of python module.
name='Ramessh lal'
def greetName():
  print(name)
greetName()
print(name)
print('###################')
def updateName():
  global name
  name='vikash lal'
  print(name)
updateName()
print(name)
print('###################')
def outer():
  def inner():
    print(name)
  inner()
  print(name)
outer()

#Built-in scope: Built-in scope contains name that Python provides e.g len(), sum() , range(),print()
print('###################')
numbers = [1,2,3,4,5]
print(sum(numbers))
print(len(numbers))



