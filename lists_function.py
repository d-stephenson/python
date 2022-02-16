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
