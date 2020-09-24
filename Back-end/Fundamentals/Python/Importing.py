''
def squared_action(base,multiply):
  result = base
  
  for i in range(multiply): 
    result = result * base 
    print(result)
 ''
 # this function stored in file named: square.py 


# IMPORT - Functions

  # importing all the funtions from a file #
  # import file_name
  import square

  # Importing Specific Function/s #
  # from file_name import function_0, function_1
  from square import squared_action
  
  # Importing + Changing Function name #
  # from file_name import function_0 as new_name
  from square import squared_action as sa
  
  # Importing + Changing File Name #
  # import file_name as new_name
  import square as sq
  
  
# using a function
# file_name.function_name()
square.squared_action()

# IMPORT - Classes
# Import a Single Class #
# From File_Name import Class_Name

# Import a multiple Classes #
# from File_Name import Class_Name, Class_Name2

# creating variables 
# variable = Class_Name("value1","value2","value3")



# Import the whole Moudle
# import File_Name 
# creating variables 
# variable = File_Name.Class_Name ("value1","value2","value3")
