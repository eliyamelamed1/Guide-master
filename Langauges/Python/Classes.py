# Creating a class # '' problem at line 11/18 ''
# class Class_Name():
class Cars():
  
  # creating class and attributes #
  # def __init__ (self, attribute_name):
  # self.attribute_name = attribute_value
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    self.car_owner = 'Eliya'
    
  # creating a function based on the class attributes
  # def Function_name(self):
  def car_details(self):
    self.details = self.brand, self.model, str(self.year)
    return self.details
    
  # an example function to modify value
  def owner(self,*new_owner):
    self.car_owner=new_owner
    return self.car_owner
    
  def fill_gas_tank():   
    print("you need to fill the gas tank!")
  
# Creating variables and assigning them values #
# Variable_Name = Class_Name(attributes_value)
car_1 = Cars("toyota","corola",2017)
car_2 = Cars("Audi","R3",2018)

# Creating a list that contains the variables
all_cars = [car_1, car_2]
car_number = 1

# Looping through the variables 
for car in all_cars:
  print (car_number)
  print (car.car_details())
  print ('\n')
  car_number += 1


# 2 ways to modify an attribute value #
# accessing the attribute directly 
# Variable_Name.Attribute = New_Value
car_1.car_owner = 'amit'

# using a function that Takes argument and set the attribute Value accordingly
# Variable_Name.Function_Name(New_Value)
car_2.owner('Harel')

  
------------------------### Inheritance ###-------------------------------

                    
# create child class
# class Child_Class(Parent_Class):
class Electric_Car(Cars):
# Initialize attributes of the parent class
  def __init__(self, brand, model, year):
  # connecting the child and the parent classes
    super().__init__(brand, model, year)
    # creating child class attributes 
    self.battery_size = 70
    
    # Error needs to check that out
    self.battery = Battery()
    
  def show_battery(self):  
    print("This car has a " + str(self.battery_size) + "-kWh battery.")
  
  # Override parent class functions
  def fill_gas_tank():   
    print("This car doesn't need a gas tank!")

# creating Child Class variable
tesla_1 = Electric_Car("tesla", "model s", 2016)

# using parent class functions on the child class variable
print (tesla_1.car_details())
print (tesla_1.owner("Elixya", "Amit"))
tesla_1.show_battery()

# Error python crash course pdf (208-209)
class Battery():
  def __init__ (self, battery_size ):
    self.battery_size = battery_size 
       
  def show_battery(self):  
    print("This car has a " + str(self.battery_size) + "-kWh battery.")
tesla_1.battery.show_battery()



---------------------# Class methods #------------------------
                   
class Vehicles():
  number_of_vehicles = 0
  
  def __init__ (self, name):
    self.name = name
    Vehicles.add_vehicle()
  
  @classmethod
  def add_vehicle(cls)
    cls.number_of_vehicles += 1
    
  @classmethod
  def get_number_of_vehicles(cls)
    return cls.number_of_vehicles
        
    
class Math():
  
  @staticmethod
  def add100(x):
    return x += 100
    
print (math.add100(10))
    
 
  
  
