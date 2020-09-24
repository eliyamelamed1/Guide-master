     # Handling the ZeroDivisionError Exception #
print (5/0)

>>> Traceback (most recent call last):
      File "division.py", line 1, in <module>   
        print(5/0) 
    ZeroDivisionError: division by zero 
    
# Solution

try:
  print (5/0)
  
except ZeroDivisionError:
  print ("You can't divide by zero!")
  
>>> You can't divide by zero!

     # Handling the FileNotFoundError Exception #
     
try:   
  with open(filename) as f_obj:   
    contents = f_obj.read() 
except FileNotFoundError:    
  msg = "Sorry, the file " + filename + " does not exist."     
  print(msg)
  
  
 # excepting silently
 try:   
  with open(filename) as f_obj:   
    contents = f_obj.read() 
except FileNotFoundError:    
  pass
  
  
