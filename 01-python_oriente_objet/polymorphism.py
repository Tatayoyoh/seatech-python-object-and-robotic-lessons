import sys
import time

def colored(text):
    return "\033[1m\033[93m%s\033[0m"%(text)

class Robot():
    """
        Simple Robot made to say Hello/Goodbye
    """

    __running = False

    # protected
    def _process_action(self, msg):
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(1)

    @property
    def is_running(self):
        return self.__running

    def start(self):
        self.__running = True
        
    def stop(self):
        self.__running = False
      
    def start_mission(self):
        print("Hello ! I'm a simple Robot.")
        self.start() 

    def stop_mission(self):
        print("Goodbye ! From simple Robot.")
        self.stop() 
  
class UnmannedVehicle(Robot):
    """
        A vehicule half autonomous, made to execute a given mission
    """

    __mission = None

    @property
    def mission(self):
        return self.__mission

    # protected
    def _safety_checks(self):
        self._process_action('Code safety checks... ')
        self._process_action('OK\n')
        self._process_action('Mecanic safety checks... ')
        self._process_action('OK\n')
        self._process_action('Electronic safety checks... ')
        self._process_action('OK\n')

    # protected
    def _integrity_checks(self):
        self._process_action('Mission data integrity checks... ')
        self._process_action('OK\n')
        self._process_action('Mecanic integrity checks... ')
        self._process_action('OK\n')
        self._process_action('Electronic integrity checks... ')
        self._process_action('OK\n')

    # protected
    def _run_mission(self):
        self.start()
        self._process_action('Mission <%s> is running\n'%(colored(self.__mission)))

    # protected
    def _safe_stop(self):
        self._process_action('Process to a secure system stop... ')
        self.stop()
        self._process_action('OK\n')

    def plan_mission(self, mission):
        if type(mission) is not str: # some weak checks...
            print('Mission format is not valid')
            return False
        self.__mission = mission
        print('Mission <%s> is validated and set as default'%(colored(self.mission)))
        return True

    def start_mission(self, mission=None):
        if not self.is_running and (self.mission or self.plan_mission(mission)):
            print('Mission <%s> will start after safety checks'%(colored(self.mission)))
            self._safety_checks()
            self._run_mission()
    
    def stop_mission(self):
        if self.is_running:
            self._safe_stop()
            print('Mission <%s> was stopped'%(colored(self.mission)))
            self._integrity_checks()
  
class UnmannedUnderwaterVehicle(UnmannedVehicle):
    """
        An underwater vehicule half autonomous, made to execute a given mission
    """
    __is_underwater = False

    @property
    def is_underwater(self):
        return self.__is_underwater
    
    def __dive(self):
        self._process_action("Let's go undersea captain !... ")
        self.__is_underwater = True
        self._process_action('Dive OK\n')
    
    def __surface(self):
        self._process_action("Let's sea the sky captain !... ")
        self.__is_underwater = False
        self._process_action('Surface OK\n')
    
    def _run_mission(self):
        self.__dive()
        super()._run_mission()

    def _safe_stop(self):
        self.__surface()
        super()._safe_stop()

if __name__ == '__main__':
    # Play with Robot parent class
    print('\n\n[Robot]\n')
    r = Robot()
 
    r.start_mission()
 
    if r.is_running:
        print('Robot is running')
 
    r.stop_mission()

    # Play with UnmannedVehicle parent class
    print('\n\n[UnmannedVehicle]\n')
    uv = UnmannedVehicle()
    uv.plan_mission('Collect data from your environment')

    uv.start_mission()

    if uv.is_running:
        print('UnmannedVehicle is running\n')

    uv.stop_mission()

    # Play with UnmannedUnderwaterVehicle child class
    print('\n[UnmannedUnderwaterVehicle]\n')
    uuv = UnmannedUnderwaterVehicle()
    
    uuv.plan_mission('Collect underwater data from your environment')

    uuv.start_mission()

    if uuv.is_running:
        print('UnmannedVehicle is running\n')

    uuv.stop_mission()