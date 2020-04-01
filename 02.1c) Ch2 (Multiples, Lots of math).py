### First 3 Multiples ###
def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3
first_three_multiples(10)
###############################
### Tip based on a given percentage and total amount ###
def tip(total, percentage):
  f = total * percentage/100
  return f
print(tip(10, 25))
###############################
### Writing last, first and last name, James Bond style ###
def introduction(first_name, last_name):
  f = last_name + ", " + first_name + " " + last_name
  return f
print(introduction("James", "Bond"))
### OR ###
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name    # without assigning to f: But do assign
print(introduction("James", "Bond"))
###############################
### writing a string telling age 7 times the given age ###
def dog_years(name, age):
  return name+", you are "+str(age*7)+" years old in dog years"
print(dog_years("Lola", 16))
### OR
def dog_years(name, age):
  f =  name+", you are "+str(age*7)+" years old in dog years"
  return f
print(dog_years("Lola", 16))
################################
#Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
#First, print the sum of a and b.
#Second, print d subtracted from c.
#Third, print the first number printed, multiplied by the second number printed.
#Finally, return the third number printed mod a
def lots_of_math(a, b, c, d):
  first = a+b
  second = c-d
  third = first*second
  fourth = third%a
  print(first)                         #Cannot print and save simultaneously
  print(second)
  print(third)
  return fourth

print(lots_of_math(1, 2, 3, 4))
####################################################################################################

