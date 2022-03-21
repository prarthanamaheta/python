# @property decorator with getter and setter method

# # 1 simple code
# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

# human = Celsius()
# human.temperature=37
# print(human.temperature)
# print(human.to_fahrenheit())

# Whenever we assign or retrieve any object attribute like temperature as shown above, 
# Python searches it in the object's built-in __dict__ dictionary attribute.



# we want to extend the usability of the Celsius class defined above. 
# We know that the temperature of any object cannot reach below -273.15 degrees Celsius
# An obvious solution to the above restriction will be to hide the attribute temperature 
# (make it private) and define new getter and setter methods to manipulate it.


# Furthermore, temperature was replaced with _temperature. 
# An underscore _ at the beginning is used to denote private variables in Python.

# 2 using getter setter
# # Making Getters and Setter methods
# class Celsius:
#     def __init__(self, temperature=0):
#         self.set_temperature(temperature)

#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32

#     # getter method
#     def get_temperature(self):
#         return self._temperature

#     # setter method
#     def set_temperature(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature below -273.15 is not possible.")
#         self._temperature = value


# # Create a new object, set_temperature() internally called by __init__
# human = Celsius(37)

# # Get the temperature attribute via a getter
# print(human.get_temperature())

# # Get the to_fahrenheit method, get_temperature() called by the method itself
# print(human.to_fahrenheit())

# # new constraint implementation
# human.set_temperature(-300)

# # Get the to_fahreheit method
# print(human.to_fahrenheit())


# problem- implemented our previous class have to modify their code 
# from obj.temperature to obj.get_temperature() and 
# all expressions like obj.temperature = val to obj.set_temperature(val).

# This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.
# All in all, our new update was not backwards compatible. This is where @property comes to rescue.
#provide read only attribute

# 3 Property  object
# using property class
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

#     # getter
#     def get_temperature(self):
#         print("Getting value...")
#         return self._temperature

#     # setter
#     def set_temperature(self, value):
#         print("Setting value...")
#         if value < -273.15:
#             raise ValueError("Temperature below -273.15 is not possible")
#         self._temperature = value

#     # creating a property object
#     temperature = property(get_temperature, set_temperature)


# human = Celsius(37)

# print(human.temperature)

# print(human.to_fahrenheit())

# human.temperature = -300

# As we can see, any code that retrieves the value of temperature will automatically call get_temperature() 
# instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to temperature will
#  automatically call set_temperature().

# We can even see above that set_temperature() was called even when we created an object. 

# why??????

# The reason is that when an object is created, the __init__() method gets called. 
# This method has the line self.temperature = temperature.
#  This expression automatically calls set_temperature()

# The @property Decorator
# In Python, property() is a built-in function that creates and returns a property object. 

# property(fget=None, fset=None, fdel=None, doc=None)

# temperature = property(get_temperature,set_temperature)


# # make empty property
# temperature = property()
# # assign fget
# temperature = temperature.getter(get_temperature)
# # assign fset
# temperature = temperature.setter(set_temperature)

# We can even not define the names get_temperature and set_temperature as
# they are unnecessary and pollute the class namespace.

# For this, we reuse the temperature name while defining our getter and setter functions.

# 4 property with same name of methods
# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...") 
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
