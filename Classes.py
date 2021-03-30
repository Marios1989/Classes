# Intro
class Animal(object):
    pass

# Classier Classes
class Animal(object):
    def __init__(self):
        pass

# Let's Not Get Too Selfish
class Animal(object):
 def __init__(self, name):
    self.name = name

# Instantiating Your First Object
class Animal(object):
    def __init__(self, name):
        self.name = name


zebra = Animal("Jeffrey")

print(zebra.name)

# More on __init__() and self
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

# A Methodical Approach
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)

# They're Multiplying!
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)
hippo = Animal("Jeffrey", 5)
sloth = Animal("Tom", 3)
ocelot = Animal("Jake", 2)
print(hippo.name, hippo.age, hippo.is_alive, hippo.health)
print(sloth.name, sloth.age, sloth.is_alive, sloth.health)
print(ocelot.name, ocelot.age, ocelot.is_alive, ocelot.health)

# It's Not All Animals and Fruits
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print(product + " added.")
    else:
      print(product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print(product + " removed.")
    else:
      print(product + " is not in the cart.")
my_cart = ShoppingCart("Marios")
my_cart.add_item("Cup", 9)

# Inheritance Syntax
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

# Override!
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

# This Looks Like a Job For...
class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)


milton = PartTimeEmployee('Milton')
print(milton.full_time_wage(10))

# Class Basics
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

# Class It Up
class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

# Instantiate an Object
class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


my_triangle = Triangle(30, 60, 90)

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

# Inheritance
class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

