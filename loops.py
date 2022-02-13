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

# Dictionary

# A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces, like so:
# d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth'] 
print residents['Burmese Python']

#--------------------------------

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Bacon Cheese Burger'] = 10.50 
menu['Pesto Pasta'] = 12.50 
menu['Southern Fried Wrap'] = 14.50 

print "There are " + str(len(menu)) + " items on the menu."
print menu

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Jungle House'

print zoo_animals


# Remove from List

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')

print backpack

#--------------------------------

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]

#--------------------------------

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry','lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] = inventory['gold'] + 50

print inventory





