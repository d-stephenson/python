# While

# The while loop is similar to an if statement: it executes the code 
# inside of it if some condition is true. The difference is that the 
# while loop will continue to execute as long as the condition is true
# In other words, instead of executing if something is true, it executes 
# while that thing is true

count = 0

if count < 5:
  print "Hello, I am an if statement and count is", count

while count < 5:
  print "Hello, I am a while and count is", count
  count += 1
  
# The condition is the expression that decides whether the loop is going 
# to continue being executed or not. There are 5 steps to this program

loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False
  
num = 1

while num < 11:  # Fill in the condition
  # Print num squared
  # Increment num (make sure to do this!)
  print num ** 2
  num +=1
  
choice = raw_input('Enjoying the course? (y/n)')

while choice != "y" and choice != "no": 
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

# While / else

# while/else is similar to if/else, but there is a difference: the else block 
# will execute anytime the loop condition is evaluated to False. This means that 
# it will execute if the loop is never entered or if the loop exits normally. If 
# the loop exits as the result of a break, the else will not be executed

# In this example, the loop will break if a 5 is generated, and the else will not 
# execute. Otherwise, after 3 numbers are generated, the loop condition will become 
# false and the else will execute

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
  
from random import randint

#--------------------------------

random_number = randint(1, 10)
guesses_left = 3
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  print guess
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."

#--------------------------------
  
print "Counting..."

for i in range(20):
  print i

#--------------------------------

hobbies = []
for num in range(3):
  hobby = raw_input("Your hobby: ")
  hobbies.append(hobby)
  print hobbies
  
#--------------------------------

thing = "spam!"

for c in thing:
  print c

word = "eggs!"

for c in word:
  print c

# String manipulation

# word = "Marble"
# for char in word:
#   print char,

# The example above iterates through each character in word and, in the end, prints 
# out M a r b l e.
# The , character after our print statement means that our next print statement 
# keeps printing on the same line.

phrase = "A bird in the hand..."
for char in phrase:
  if char == "A" or char == "a":
    print "X",
  else:
    print char,

print

# For your lists

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

for num in numbers:
  print num ** 2
  
# Looping over a dictionary

# You may be wondering how looping over a dictionary would work. Would you get the 
# key or the value?
# The short answer is: you get the key which you can use to get the value.

d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print "This dictionary has the value 10!"
    
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
  print key, d[key]

#--------------------------------

# enumerate works by supplying a corresponding index to each element in the list that you pass it

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item
  
#--------------------------------

# Multiple lists

# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
 if a > b:
   print a
 else:
   print b 