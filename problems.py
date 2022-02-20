# Problems

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False

print is_even(26572)

#--------------------------------

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)

#--------------------------------

# summing the digits of a number

number = 123129

def digit_sum(n):
  result = sum(int(digit) 
  for digit in str(n))
  return result
print digit_sum(number)

#--------------------------------

# factorial [recursion]

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 7
result = factorial(num)
print ("The factorial of", num, "is", result)

#--------------------------------

# is_prime