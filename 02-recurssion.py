def recur(num):
  print('calling recursion',num)
  if(num==5):
    return
  recur(num+1)

# recur(1)

# Factorial of a number
def factorial(num):
  if( num==1):
    return 1
  result =num * factorial(num-1)
  return result
print('factorial of given number is ',factorial(3))