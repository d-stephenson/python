print "Hi"

print "Hi " + "Dale"

#SyntaxError: EOL while scanning a string literal

#print "Mismatched quotes will cause a SyntaxError'
#print Without quotes will cause a NameError

print("How do you make a hot dog stand?")
print('You take away its chair!')

#Create a variable 

greeting_message = "Welcome to Codecademy!"
current_excercise = 5

#--------------------------------

#Python also offers a companion to division called the modulo operator. The modulo operator is indicated by % and returns the remainder after division is performed

is_this_number_odd = 15 % 2
is_this_number_divisible_by_seven = 133 % 7

#In the above code block, we use the modulo operator to find the remainder of 15 divided by 2. Since 15 is an odd number the remainder is 1

product = 28 * 145
remainder = 1398 % 11

print product
print remainder

#Updating variables

money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price
 
sandwich_price += sales_tax
money_in_wallet -= sandwich_price

print money_in_wallet 
print sandwich_price

#--------------------------------

january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

print annual_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

print annual_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

print annual_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += september_rainfall
annual_rainfall += october_rainfall
annual_rainfall += november_rainfall
annual_rainfall += december_rainfall

print annual_rainfall

#--------------------------------

#Integer, which is a whole number with no decimal point

int1 = 1
int2 = 10
int3 = -5

#A number with a decimal point is called a float

float1 = 1.0
float2 = 10.
float3 = -5.5

print float2

#You can also define a float using scientific notation, with e indicating the power of 10
# this evaluates to 150:

float4 = 1.5e2 

print float4

#--------------------------------

cucumbers = 4
price_per_cucumber = 3.25
total_cost = price_per_cucumber * cucumbers 
print total_cost

#--------------------------------

#if the numbers do not divide evenly, the result of the division is truncated into an integer. In other words, the quotient is rounded down to a whole number

quotient1 = 6/2 #Answer = 3
print quotient1

quotient2 = 7/2 #Answer = 3
print quotient2

#To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float

quotient3 = 7./2
print quotient3
# the value of quotient1 is 3.5
quotient4 = 7/2.
print quotient4
# the value of quotient2 is 3.5
quotient5 = 7./2.
print quotient5
# the value of quotient3 is 3.5

#Or float() method
quotient6 = float(7)/2
print quotient6

#--------------------------------

cucumbers = 100
num_people = 6

whole_cucumbers_per_person = cucumbers/num_people

print whole_cucumbers_per_person

float_cucumbers_per_person = float(cucumbers)/num_people

print float_cucumbers_per_person

#--------------------------------

#Multi-line Strings

haiku = """The old pond,
A frog jumps in:
Plop!"""

print haiku

#--------------------------------

#Booleans

a = True
b = False

#--------------------------------

# Value Error

# A variable with the value 

# 7 is an integer
# 7. is a float
# "7" is a string

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)

print product
print big_string

number1 = "100"
number2 = "10"

print int(number1)
print float(number1)
 
string_addition = number1 + number2 
#string_addition now has a value of "10010"
 
int_addition = int(number1) + int(number2)
#int_addition has a value of 110

print string_addition
print int_addition 

#--------------------------------

#The amount of points for each exercise may change, because points don't exist yet
skill_completed = "Python Syntax"
exercises_completed = 13
points_per_exercise = 5
point_total = 100 + (exercises_completed * points_per_exercise)

print "I got " + str(point_total) + " points!"

#--------------------------------

#Escaping characters \

# print 'There's a snake in my boot!'
print 'There\'s a snake in my boot!'

#Access by Index

fifth_letter = "MONTY"[4]
print fifth_letter

#--------------------------------

#String methods

parrot = "Norwegian Blue"
print len(parrot)

parrot1 = "Norwegian Blue".lower()
print parrot1

parrot2 = "Norwegian Blue"
print parrot1.upper()

pi = 3.14
print str(pi)

#--------------------------------

#Dot Notation
# Methods that use dot notation only work with strings
# On the other hand, len() and str() can work on other data types

ministry = "The Ministry of Silly Walks"
print len(ministry)
print ministry.upper()

#--------------------------------

#String Concatenation

# The % operator after the string is used to combine a string with variables
# The % operator will replace the %s in the string with the string variable that comes after it

string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

day = 6
print "03 - %s - 2019" % (day)
# 03 - 6 - 2019
print "03 - %02d - 2019" % (day)
# 03 - 06 - 2019

# String Formatting with %
# You need the same number of %s terms in a string as the number of variables in parentheses

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)

my_string = "Sunshine"
print len(my_string)
print my_string.upper()

#--------------------------------

# The datetime Library
# A lot of times you want to keep track of when something happened. We can do so in Python using datetime.

# Getting the Current Date and Time
# We can use a function called datetime.now() to retrieve the current date and time.

from datetime import datetime
print datetime.now()

from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print current_year 
print current_month 
print current_day 

from datetime import datetime
print datetime.now()
now = datetime.now()
print now.year
print now.month
print now.day

# Remember that the standalone % operator after the string will fill the %02d and %04d placeholders in the string on the left with the numbers 
# and strings in the parentheses on the right.
# %02d pads the month and day numbers with zeros to two places, and %04d pads the year to four places. 

from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d' % (now.month, now.day, now.year)
print '%02d-%02d-%04d' % (now.month, now.day, now.year)

print now.hour
print now.minute
print now.second

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

# Control flow gives us this ability to choose among outcomes based on what else is happening in the program.

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

# Comparators
# There are six:

# Equal to (==)

# >>> 2 == 2
# True
# >>> 2 == 5
# False
# Not equal to (!=)

# >>> 2 != 5
# True
# >>> 2 != 2
# False
# Less than (<)

# >>> 2 < 5
# True
# >>> 5 < 2
# False
# Less than or equal to (<=)

# >>> 2 <= 2
# True
# >>> 5 <= 2
# False 
# Greater than (>)

# >>> 5 > 2
# True
# >>> 2 > 5
# False
# Greater than or equal to (>=)

# >>> 5 >= 5
# True
# >>> 2 >= 5
# False
# Comparators check if a value is (or is not) equal to, greater than (or equal to), or less than (or equal to) another value.

# Note that == compares whether two things are equal, and = assigns a value to a variable.

# Boolean

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 7 == 1290

# Make me true!
bool_three = 12.9995 != 13

# Make me false!
bool_four = 27 < 1.987

# Make me true!
bool_five = 34 >= 33.2