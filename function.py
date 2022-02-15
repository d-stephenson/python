# Functions

def tax(bill):
    #   """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
    #   """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

# Define your spam function starting on line 5. You
# can leave the code on line 10 alone for now--we'll
# explain it soon!

def spam():
#   """Prints 'Comment' to the console"""
  print "Eggs!"

spam()

#--------------------------------

def square(n):
#   """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)

#--------------------------------

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

#--------------------------------

# Functions calling functions

def one_good_turn(n):
      return n + 1
    
def deserves_another(m):
  return one_good_turn(m) + 2

one_good_turn(1)
print deserves_another(2)

#--------------------------------

def cube(number):
      return (number * number) * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

print cube(23)
print by_three(23)

#--------------------------------

# Function Imports

# import math 
# print math.sqrt(25)

    # # Import *just* the sqrt function from math on line 3!

# from math import sqrt

    # # Universal import can handle this for you. The syntax for this is:

# from math import *

# import math # Imports the math module
# everything = dir(math) # Sets everything to a list of things from math
# print everything # Prints 'em all!

# Built-in Function

def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#--------------------------------

maximum = max(1.2, 5, 8.9, 7, 458.1)
print maximum

minimum = min(-25.1, 34, 100, -2.1)
print minimum

absolute = abs(-42)
print absolute

#--------------------------------

# Type function

print type(42)
print type(4.2)
print type('spam')

#--------------------------------

def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry" 

print shut_down("no")

#--------------------------------

import math
print math.sqrt(13689)

#--------------------------------

def distance_from_zero(n):
  if type(n) == int or type(n) == float:
    return abs(n)
  else:
    return "Nope"

print distance_from_zero(92398.283768470920838)

#--------------------------------

def bigger(first, second):
  print max(3, 9)
  return True

def answer():
  return 42
  
#-------------------------------- 

def hotel_cost(nights):
  return 140 * nights
    
print hotel_cost(5)

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    "Not flights to this city"
  
print plane_ride_cost("Tampa")
  
def rental_car_cost(days):
  car = 40 * days
  if days >= 7:
    car -= 50
  elif days >= 3:
    car -= 20
  return car

print rental_car_cost(5)

def trip_cost(city, days, spending_money):
      return plane_ride_cost(city) + (rental_car_cost(days) + hotel_cost(days - 1)) + spending_money 
    
print trip_cost("Los Angeles", 5, 250)

#--------------------------------
   
prices = {
  "banana": 4, 
  "apple": 2, 
  "orange": 1.5, 
  "pear": 3
}

stock = {
  "banana": 6, 
  "apple": 0, 
  "orange": 32, 
  "pear": 15
}

for food in prices:
  print food
  print "price: %s" % prices[food]
  print "stock: %s" % stock[food]
  
total = 0
for food in prices:
  print food
  print "Total " + str(prices[food] * stock[food])
  total = total + prices[food] * stock[food]
print "Grand Total " + str(total)

#--------------------------------

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total

print compute_bill(shopping_list)

def compute_bill_1(food):
  total = 0
  for item in food:
    if stock[item] > 0:
        total = total + prices[item]
        stock[item] = stock[item] - 1  
  return total 

print compute_bill_1(shopping_list)

print stock


#--------------------------------
    # Functions are defined with three components:

    # The header, which includes the def keyword, the name of the function, and any parameters the function requires. Here’s an example:
    # def hello_world(): # There are no parameters
    
    # An optional comment that explains what the function does.
    # """Prints 'Hello World!' to the console."""
    
    # The body, which describes the procedures the function carries out. The body is indented, just like conditional statements.
    # print "Hello World!"
    
    # Here’s the full function pieced together:
    # def hello_world():
    #   """Prints 'Hello World!' to the console."""
    #   print "Hello World!"
#--------------------------------

#--------------------------------
    # def square(n):
    #     Here, n is a parameter of square. A parameter is a variable that is an input to a function. It says, “Later, when square is used, you’ll be able to input any value you want, but for now we’ll call that future value n.” A function can have any number of parameters.

    # The values of the parameters passed into a function are known as the arguments. Recall in the previous example, we called:

    # py square(10)

    # Here, the function square was called with the parameter n set to the argument 10.

    # Typically, when you call a function, you should pass in the same number of arguments as there are parameters.
#--------------------------------

#--------------------------------
    # Careful with function modules

    # Universal imports may look great on the surface, but they’re not a good idea for one very important reason: they fill your program with a ton of variable and function names without the safety of those names still being associated with the module(s) they came from.

    # If you have a function of your very own named sqrt and you import math, your function is safe: there is your sqrt and there is math.sqrt. If you do from math import *, however, you have a problem: namely, two different functions with the exact same name.

    # Even if your own definitions don’t directly conflict with names from imported modules, if you import * from several modules at once, you won’t be able to figure out which variable or function came from where.

    # For these reasons, it’s best to stick with either import module and type module.name or just import specific variables and functions from various modules as needed.
#--------------------------------

#--------------------------------
    # The abs() function returns the absolute value of the number it takes as an argument—that is, that number’s distance from 0 on an imagined number line. For instance, 3 and -3 both have the same absolute value: 3. The abs() function always returns a positive value, and unlike max() and min(), it only takes a single number.
#--------------------------------