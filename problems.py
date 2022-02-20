# Problems

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False

print is_even(26572)

#--------------------------------

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)

#--------------------------------

# summing the digits of a number

number = 123129

def digit_sum(n):
  result = sum(int(digit) 
  for digit in str(n))
  return result
print digit_sum(number)

#--------------------------------

# factorial [recursion]

def factorial(x):
  if x == 1:
    return 1
  else:
    return (x * factorial(x-1))
num = 9
result = factorial(num)
print ("The factorial of", num, "is", result)

#--------------------------------

# is_prime

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1): # Start from 2 finish at x minus 1
            if x % n == 0:
                return False
        return True

print is_prime(13)
print is_prime(10)

#--------------------------------

# reverse

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
print reverse("Hello")

#--------------------------------

# anti_vowel

def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
        if char not in vowels:
            result += char
    return result
print anti_vowel("Borrow book please sir")

#--------------------------------

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

print scrabble_score("piZZa")
