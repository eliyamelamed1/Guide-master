                        # Sets #

# Set is a starcture that is able to conatain all types of types #
# * values in set is mixed ordered
# * sets DOESN'T contain duplicate values
  
# Creating sets
alltypes = {"one",1,1.1,True}

# Converting list into set
alltypes = set(["one",1,1.1,True])

# create empty set
emptyset = set()

# only while using the set() with a string he is separated 
a = set('hi') # 'hi' --> 'h','i'

# Add #
alltypes.add("C++")

# Remove #
alltypes.remove("C++")
# even if you discard value that not in set you wont get error
alltypes.discard("something that not in set")
# remove and return value
alltypes.pop()
# remove all values
alltypes.clear()



                       # Dictionaries #
# dictionary is a structure that is used to assign multiply values to a key


# Create empty dict
emptydict = {}
 ''or''
emptydict = dict() # 'hi' ==> 'h','i'
                   
# Create dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}
  
person2 = dict(first_name='Sara', last_name='Williams')

# dictionary in a dictionary
users = {
'aeinstein': {       
  'first': 'albert',       
  'last': 'einstein',         
  'location': 'princeton',         
},
'mcurie': {         
  'first': 'marie',         
  'last': 'curie',         
  'location': 'paris',
}

# List in dictionary
pizza = {
 'crust': 'thick',    
 'toppings': ['mushrooms', 'extra cheese'],   
}

# first name = key
# john = value
# first name : john = item

# Add key/value
person['phone'] = '555-555-5555'

# Remove item
del(person['age'])
person.pop('phone')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Clear list
person.clear()

# Get length
print(len(person2))


  
