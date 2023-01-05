class Robot():
  def __init__(self, name, size):
    self.name = name
    self.size = size
  
  def __str__(self): # must return a string
    return "Robot %s [size: %s]"%(self.name, self.size)
  
  def __repr__(self): # must return a string
    return str({"name":self.name, "size":self.size})


rob = Robot('Terminator', 'medium')

# __str__ call
print('> __str__ call')
print(str(Robot))
print(str(rob)) 
print(rob,'\n') # print auto convert into string

# __repr__ call
print('> __repr__ call')
print(repr(Robot))
print(repr(rob))

# In python command interpreter repr() is automatically called. 
# Nothing will be displayed in script executiobn context
rob 

