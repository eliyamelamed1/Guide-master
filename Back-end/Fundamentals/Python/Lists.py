# CREATING #

  # Creating a tuple
  dimensions = (200,50)

  # lists of dictionaries
  alien_0 = {'color': 'green', 'points': 5}
  alien_1 = {'color': 'yellow', 'points': 10} 
  aliens = [alien_0, alien_1]

  people =
  [
      {'name': 'Martha', 'age': 30},
      {'name': 'Kevin', 'age': 25}
  ]
  print(people[1]['name'])

  # Creating a simple list
  cars = ['bmw', 'audi', 'toyota', 'subaru']
  digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  
  # Creating list with value Separated
  car = list('BMW') # output - ['B','M','W']
  
    
# Adding Elements to a List #
  
  # appending Elements to the End of a List
  cars.append('value')
    
  # Inserting Elements to position in a list
  cars.insert(num,'value')

# Removing elements from a list #
   
  # removing Elements from position in a list
  del cars[num]
  
  # removing an Element and getting his value
  cars.pop()
  cars.pop(num)
    
  # removing an Item by Value  
  cars.remove('value')
  
  # Remove Duplicates from a List
  car = (list(set(car)))
  
# ORGINAZING A LIST #
  
  # Sorting a List Permanently
  cars.sort()
    
  # Sorting a List Temporarily
  print (sorted(cars))
    
  # reversing a list
  cars.sort(reverse=True)
  cars.reverse()

# working with Part of a list
  # cars[startAt:endBefore:skip]
  print(cars[1])
  print(cars[:3])
  print(cars[::2])
     
# Copying a list
vehicles = cars[:]
 
# linking 2 lists
vehicles = cars

# Find list length
len(cars)
    
# minimum, maximum and sum
min(digits)
max(digits)
sum(digits)
  
# List Comprehensions
squares = [value**2 for value in range(1,11)]

# checking if list isn't empty}
if cars:
  
# Accessing Elements in a List
cars[0]
cars['trek']
 
# Modifying Values in a List
cars[0]='value'
