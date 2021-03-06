# Implement a class to hold room information. This should have name and
# description attributes.
import items, monsters

class Room:
  def __init__(self, name, description, monster=[], inventory=[]):
    self.name = name
    self.description = description
    self.monster = monster
    self.inventory = inventory
   

  def __str__(self):
    output = "You have entered..." + str(self.name)
    output += "\n" + self.description
    output += "\nItems:"
    for i in self.inventory:
      output += i + ', ' 
    
    output += "\nMonster:"
    for i in self.monster:
      output += i + ', ' 
    return output
    
  def take_item(self, item):
    for i in self.inventory:
      output += "n " + i
    return output
    
              
