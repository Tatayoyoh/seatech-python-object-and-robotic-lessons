class Robot():
  def __init__(self, data):
    self.data = data
    self.index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= len(self.data):
      raise StopIteration
    data = self.data[self.index]
    self.index += 1
    return data

  def __destroy__(self):
    pass

  def __add__(self, robot):
    return Robot(self.data + robot.data)

  def __str__(self):
    return '[Robot: %s]' % self.data

  def __eq__(self, robot):
    print(self.data.sort())
    print(robot.data.sort())
    return self.data.sort() == robot.data.sort()
"""
def __repr__(self):
                return '[repr- data: %s]' %self.data

        def __call__(self, *args, **kwargs):
                print("I've just called:", args, kwargs)

'__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__'
"""

r = Robot(['spam','foo','bar'])
for robot_data in r:
  print(robot_data)

print(dir(Robot))

r2 = r + Robot(['other'])

print(r2)

r3 = Robot(['spam','foo','bar','other'])

print("r2 == r3 ? %s"%(r2 == r3))

print(r2)
print(r3)