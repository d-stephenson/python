# Loops

# If you want to do something with every item in the list, you can use a for loop
# A variable name follows the for keyword; it will be assigned the value of each list item in turn.
# Then in list_name designates list_name as the list the loop will work on. The line ends with a colon (:) and the indented code that follows it will be executed once per item in the list.

# for variable in list_name:
      # Do stuff!
      
#--------------------------------

my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print 2 * number
  
# Each list item is assigned to the user-defined variable number in turn. All you need to do is print two times number in the body of the loop (the indented part).
# The for loop will automatically execute your code as many times as there are items in my_list!

start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
  square_list.append(x ** 2)

square_list.sort() 

print square_list

#--------------------------------

# A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces, like so:
# d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth'] 
print residents['Burmese Python']