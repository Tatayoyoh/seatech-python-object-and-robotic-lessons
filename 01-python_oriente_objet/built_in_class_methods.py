SIZES = {'small':1, 'medium':2, 'big':3}

class Robot():
  """ My robot documentation 
  is 
  awesome 
  """

  def __init__(self, name, payloads=[], size='medium'):
    self.name = name
    self.size = size if type(size) is int else SIZES[size]
    self.size_str = size
    self.payloads = payloads

  def __iter__(self):
    self.iter_index = 0
    return self

  def __next__(self):
    if self.iter_index >= len(self.payloads):
      raise StopIteration
    payload = self.payloads[self.iter_index]
    self.iter_index += 1
    return payload

  def __add__(self, robot):
    return Robot(self.name, payloads=self.payloads + robot.payloads, size=self.size + robot.size)

  def __str__(self):
    return '%s (%s): %s' %(self.name, self.size, self.payloads)

  def __eq__(self, robot): # equal
    return (self.size == robot.size)

  def __ne__(self, robot): # not equal
    return (self.size != robot.size)

  def __gt__(self, robot): # greater than
    return (self.size > robot.size)

  def __ge__(self, robot): # greater or equal
    return (self.size >= robot.size)

  def __lt__(self, robot): # less than
    return (self.size < robot.size)

  def __le__(self, robot): # less or equal
    return (self.size <= robot.size)



if __name__ == '__main__':
    
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

  input('ENTER to display help')

  print('\nDocumentation:', help(megazord))