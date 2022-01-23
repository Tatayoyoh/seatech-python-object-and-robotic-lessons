import sys
import time

def colored(text):
    return "\033[1m\033[93m%s\033[0m"%(text)

class Robot():
    """
        Simple Robot made to say Hello/Goodbye
    """

    # protected
    _running = False

    # public
    @property
    def is_running(self):
        return self._running

    # protected
    def _process_action(self, msg):
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(1)

    # public
    def start_mission(self):
        self._process_action("Hello ! I'm a simple Robot.")
        self._running = True

    # public
    def stop_mission(self):
        self._running = False
        self._process_action("Goodbye ! From simple Robot.")
  
class UnmannedVehicle(Robot):
    """
        A vehicule half autonomous, made to execute a given mission
    """

    _mission = None

    @property
    def mission(self):
        return self._mission

    # private
    def _safety_checks(self):
        self._process_action('Code safety checks... ')
        self._process_action('OK\n')
        self._process_action('Mecanic safety checks... ')
        self._process_action('OK\n')
        self._process_action('Electronic safety checks... ')
        self._process_action('OK\n')

    # private
    def _integrity_checks(self):
        self._process_action('Mission data integrity checks... ')
        self._process_action('OK\n')
        self._process_action('Mecanic integrity checks... ')
        self._process_action('OK\n')
        self._process_action('Electronic integrity checks... ')
        self._process_action('OK\n')

    # private
    def _run_mission(self):
        self._running = True
        self._process_action('Mission <%s> is running\n'%(colored(self._mission)))

    def _safe_stop(self):
        self._process_action('Process to a secure system stop... ')
        self._running = False
        self._process_action('OK\n')

    # public
    def plan_mission(self, mission):
        if type(mission) is not str: # some weak checks...
            print('Mission format is not valid')
            return False
        self._mission = mission
        print('Mission <%s> is validated and set as default'%(colored(self._mission)))
        return True

    # public
    def start_mission(self, mission=None):
        if not self.is_running and (self._mission or self.plan_mission(mission)):
            print('Mission <%s> will start after safety checks'%(colored(self._mission)))
            self._safety_checks()
            self._run_mission()
    
    # public
    def stop_mission(self):
        if self.is_running:
            self._safe_stop()
            print('Mission <%s> was stopped'%(colored(self._mission)))
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

    # private
    def _safety_checks(self):
        self._process_action('Code safety checks... ')
        self._process_action('OK\n')
        self._process_action('Mecanic safety checks... ')
        self._process_action('OK\n')
        self._process_action('Electronic safety checks... ')
        self._process_action('OK\n')

    # private
    def _integrity_checks(self):
        self._process_action('Mission data integrity checks... ')
        self._process_action('OK\n')
        self._process_action('Mecanic integrity checks... ')
        self._process_action('OK\n')
        self._process_action('Electronic integrity checks... ')
        self._process_action('OK\n')

    # private
    def _run_mission(self):
        self.__dive()
        self._running = True
        self._process_action('Mission <%s> is running\n'%(colored(self._mission)))

    def _safe_stop(self):
        self.__surface()
        self._process_action('Process to a secure system stop... ')
        self._running = False
        self._process_action('OK\n')

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
    print()
    uv.start_mission()
    if uv.is_running:
        print('UnmannedVehicle is running\n')
    uv.stop_mission()

    # Play with UnmannedUnderwaterVehicle child class
    print('\n[UnmannedUnderwaterVehicle]\n')
    uuv = UnmannedUnderwaterVehicle()
    uuv.plan_mission('Collect underwater data from your environment')
    print()
    uuv.start_mission()
    if uuv.is_running:
        print('UnmannedVehicle is running\n')
    uuv.stop_mission()