                # Reading from a file #
                               
# Opening a file
with open (file_name.txt) as file_object:
# Reading an Entire File
  contents = file_object.read()    
  print(contents)
# Reading Line by Line.
  for line in file_object: 
    print(line)
# Making a list of lines
  lines = file_object.readlines()
        
        
    # Opening file from a different dictionary #
    
    
# Linux + Mac
with open('text_files/file_name.txt') as file_object:
#OR
# Windows
with open('text_files\file_name.txt') as file_object:
  
    # Opening file fron specific file path #
# Linux + Mac
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt
with open(file_path) as file_object:
  
# Windows
# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
           
       
               #  Writing to a file #
              
filename = 'file_name.txt'
# Writing to an empty file
with open(filename, 'w') as file_object:
  file_object.write("new text")
# appending to existing file
with open(filename, 'a') as file_object:   
 file_object.write("more text") 


                   # Storing Data #                  
import json

# store in file
name = input("what is your name?")
filename = 'name.json'
with open(filename, 'w') as f_obj: 
    json.dump(name, f_obj)

# read file
filename = 'name.json'
with open(filename) as f_o
    name = json.load(f_obj)
print (name)


   
