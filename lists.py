# Lists

zoo_animals = ["pangolin", "cassowary", "sloth", "lion"];
# One animal is missing!

if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3] 

#--------------------------------

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "elephant"

print zoo_animals

#--------------------------------

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shorts")
suitcase.append("flip flops")
suitcase.append("hat")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

#--------------------------------

# In Python, when we specify a portion of a list in this manner, we include the element with the first index, 1, but we exclude the element with the second index, 3.

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last = suitcase[4:6] 