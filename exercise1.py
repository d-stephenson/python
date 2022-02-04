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

