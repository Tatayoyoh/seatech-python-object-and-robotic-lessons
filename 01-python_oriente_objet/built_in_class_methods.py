
class Robot():
  """ My robot documentation 
  is 
  awesome 
  """
  __SIZES = {'small':1, 'medium':2, 'big':3}

  def __init__(self, name, payloads=[], size='medium'):
    self.name = name
    self.size = size
    self.payloads = payloads
    self.payloads_index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.payloads_index >= len(self.payloads):
      raise StopIteration
    payloads = self.payloads[self.payloads_index]
    self.payloads_index += 1
    return payloads

  def __add__(self, robot):
    return Robot(self.name, payloads=self.payloads + robot.payloads, size=self.size)

  def __str__(self):
    return '%s (%s): %s' %(self.name, self.size, self.payloads)

  def __eq__(self, robot): # equal
    return (self.__SIZES[self.size] == self.__SIZES[robot.size])

  def __ne__(self, robot): # not equal
    global __SIZES
    return (self.__SIZES[self.size] != self.__SIZES[robot.size])

  def __gt__(self, robot): # greater than
    return (self.__SIZES[self.size] > self.__SIZES[robot.size])

  def __ge__(self, robot): # greater or equal
    return (self.__SIZES[self.size] >= self.__SIZES[robot.size])

  def __lt__(self, robot): # less than
    return (self.__SIZES[self.size] < self.__SIZES[robot.size])

  def __le__(self, robot): # less or equal
    return (self.__SIZES[self.size] <= self.__SIZES[robot.size])


# Let's call power rangers robots !
blue = Robot('PowerRanger Blue robot', payloads=['camera'])
yellow = Robot('PowerRanger Yellow robot ', payloads=['gun'])
red = Robot('PowerRanger Red robot', payloads=['radar'])
green = Robot('PowerRanger Green robot', payloads=['wings'])

print(blue)
print(yellow)
print(red)
print(green)

print()

megazord = Robot('MEGAZORD', size='big') + blue + yellow + red + green
print(megazord)

print("Let's check MEGAZORD stuff")
for robot_payload in megazord:
  print("  * found:",robot_payload)

print()

optimus = Robot('OptimusPrime', payloads=['camera','gun','radar','wings'], size='big')
print(optimus)

print()
print("MEGAZORD == OptimusPrime ? %s" %(megazord == optimus))
print("MEGAZORD != OptimusPrime ? %s" %(megazord != optimus))
print("MEGAZORD < OptimusPrime ? %s" %(megazord < optimus))
print("MEGAZORD == PowerRanger Blue robot ? %s" %(megazord == blue))
print("PowerRanger Blue robot < OptimusPrime ? %s" %(blue < optimus))
print("OptimusPrime >= PowerRanger Blue robot ? %s" %(optimus >= blue))
print("OptimusPrime >= MEGAZORD ? %s" %(optimus >= megazord))

print()
memory_size = megazord.__sizeof__()
print("MEGAZORD takes %sbytes in memory"%(memory_size))

print('\nDocumentation:', megazord.__doc__)