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

