# List accessing

n = [1, 3, 5]

n[1] = n[1] * 5
print n

n.append(4)
print n

m = [1, 3, 5]
m.pop(1)
# Returns 3 (the item at index 1)
print "m" + str(m)

o = [1, 3, 5]
o.remove(5)
# Removes 1 from the list,
# NOT the item at index 1
print "o" + str(o)

p = [1, 3, 5]
del(p[1])
# Doesn't return anything
print "p" + str(p)

q = [1, 3, 5]
# Remove the first item in the list here
del(q[0])
print "q" + str(q)

#--------------------------------

# Changing the functionality of a function

number = 5

def my_function(x):
  return x * 3

print my_function(number)

m = 5
n = 13
# Add add_function here!
def add_function(x, y):
  return x + y

print add_function(m, n)

#--------------------------------

# Strings in functions

n = "Hello"
# Your function here!
def string_function(s):
  return s + " world"

print string_function(n)

#--------------------------------

# Lists in functions

def list_function(x):
      return x

m = [3, 5, 7]
print list_function(m)

def list_function(x):
      return x[0]

n = [3, 5, 7]
print list_function(n)

def double_first(n):
    n[0] = n[0] * 2
 
numbers = [1, 2, 3, 4]
double_first(numbers)
print numbers

# Modifying an element of a list in a function

def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print list_function(n)

my_list = [1, 2, 3]
my_list.append(4)
print my_list

n = [3, 5, 7]
def list_extender(lst):
    lst.append(9)
    return lst
print list_extender(n)

# Printing out a list item by item in a function

n = [3, 5, 7]
def print_list(x):
  for i in range(0, len(x)):
    print x[i]
  
print_list(n)

# Modifying each element in a list in a function

n = [3, 5, 7]

for i in range(0, len(n)):
  n[i] = n[i] * 2

print "Not a function " + str(n)

# Convert to this 

n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print "Function " + str(double_list(n))

# The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists

# In all cases, the range() function returns a list of numbers from start up to (but not including) stop Each item increases by step
# If omitted, start defaults to 0 and step defaults to 1

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
    return x

print my_function(range(3))

n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(0, len(numbers)):
    result += numbers[i]
  return result
    
print total(n)

n = ["Michael", "Lieberman"]

def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print join_strings(n)

#--------------------------------

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
  return x + y

print join_lists(m, n)

#--------------------------------

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print flatten(n)

#--------------------------------
    # Method 1 for item in list
    # for item in list:
    #   print item

    # Method 2 iterate through indexes
    # for i in range(len(list)):
    #   print list[i]

    # Method 1 is useful to loop through the list, but it’s not possible to modify the list this way
    # Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed Since we aren’t modifying the list, feel free to use either one on this lesson
#--------------------------------

#--------------------------------
    # Using a list of lists in a function

    # single list that contains multiple lists and how to use them in a function.

    # list_of_lists = [[1, 2, 3], [4, 5, 6]]
    
    # for lst in list_of_lists:
    #   for item in lst:
    #     print item
    # In the example above, we first create a list containing two items, each of which is a list of numbers.
    # Then, we iterate through our outer list.
    # For each of the two inner lists (as lst), we iterate through the numbers (as item) and print them out.
    # We end up printing out:

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
#--------------------------------