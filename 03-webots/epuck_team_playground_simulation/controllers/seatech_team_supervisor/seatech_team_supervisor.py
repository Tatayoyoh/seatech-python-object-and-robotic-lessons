from controller import Keyboard
from SeatechSupervisor import SeatechSupervisor

def help_text():
    print('Which mode do you want to play ?')
    print('[A] Single random controller')
    print('[B] All controllers')
    print('Enter your choice :')

if __name__ == '__main__':
    TIME_STEP = 64
    supervisor = SeatechSupervisor()

    keyboard = Keyboard()
    keyboard.enable(samplingPeriod=200)

    print('Student folder:', supervisor.students_folder)
    help_text()

    choice = None

    while supervisor.step(TIME_STEP) != -1:
        key = keyboard.getKey()
        
        if key != -1:
            key = chr(key).upper()

        if not supervisor.running:
            if key == 'A' :
                supervisor.set_single_random_controller_mode()
                print('Mode "Single random controller" activation')
            elif key == 'B':
                supervisor.set_all_controllers_mode()
                print('Mode "All controller" activation')

        if key == 'R':
            supervisor.clear()
            print('Removed all nodes')

        supervisor.update_token_positions()
