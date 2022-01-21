class Robot():
  power = False
  
  def status(self):
    print('power [%s]'%(self.power))
  
class UnmannedRobot(Robot):
  mission = '<undefined>'
  def start_mission(self):
    print('Start mission %s'%(self.mission))
  
  def status(self):
    print('power [%s], mission %s'%(self.power, self.mission))
  
class UUV(UnmannedRobot):
  is_underwater = False
  def dive(self):
    self.is_underwater = True
  
  def status(self):
    print('power [%s], mission %s, underwater [%s]'%(self.power, self.mission, self.is_underwater))

if __name__ == '__main__':
  print('\nRobot')
  r = Robot()
  r.status()
  print('power',r.power)

  print('\nUnmannedRobot')
  r = UnmannedRobot()
  print('power',r.power)
  print('mission',r.mission)
  r.status()

  print('\nUUV')
  r = UUV()
  r.status()
  print('power',r.power)
  print('mission',r.mission)
  print('is_underwater',r.is_underwater)