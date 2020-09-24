# Creating simple function
def describe_pet(animal_type, pet_name):  
  print("\nI have a " + animal_type + ".")    
  print("My " + animal_type + "'s name is " + pet_name.title() + ".") 
# Calling the function  
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('hamster','harry')

# function that return value #
def get_formatted_name(first_name, last_name):
   """Return a full name, neatly formatted."""  
  full_name = first_name + ' ' + last_name 
  return full_name.title() 
  # calling the function
  musician = get_formatted_name('jimi', 'hendrix') 
print(musician)

# function that get dictionary as an argument #
def build_profile(**user_info): 
  """Build a dictionary containing everything we know about a user."""   
    profile = {} 
    for key, value in user_info.items():       
      profile[key] = value  
    return profile 
    user_profile = build_profile
    (
      first = 'albert',
      last = 'einstein', 
      location = 'princeton',   
      field = 'physics'
    )
    print(user_profile) 


# Making an Argument  Optional
def get_formatted_name(first_name, last_name, middle_name=''):

# Creating function with default value
def describe_pet(pet_name, animal_type='dog'):

# getting multiple arguments
def make_pizza(*toppings):
  

