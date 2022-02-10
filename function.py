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