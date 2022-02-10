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
    
