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