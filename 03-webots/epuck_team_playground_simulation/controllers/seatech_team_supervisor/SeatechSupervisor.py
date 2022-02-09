from os.path import abspath, dirname, join, splitext
import os
import random, math
from controller import Supervisor, Node, Robot

class SeatechSupervisor(Supervisor):
    def __init__(self):
        super().__init__()
        self.__students_folder = abspath(join(dirname(abspath(__name__)), '..'))
        self.__running = False
        self.__robots = {}
        self.__tokens = {}
        self.__students_controllers = []
        self.__number_of_robots = 9
        self.__hunter_color = [1,0,0]
        self.__normal_color = [0,1,0]
        self.__token_z = 0.06

        self.__root_node = self.getRoot()
        self.__root_children = self.__root_node.getField('children')

        self.__get_students_controllers()

    @property
    def students_folder(self):
        return self.__students_folder

    @property
    def running(self):
        return self.__running

    def __get_students_controllers(self):
        for root, dirs, files in os.walk(self.__students_folder):
            for file in files:
                if file.endswith('_controller.py'):
                    self.__students_controllers.append(splitext(file)[0])
        print('Found controllers :\n\t', '\n\t'.join(self.__students_controllers))

    def __set_catcher(self):
        catcher_robot = 'SEATECH-%s'%(random.randrange(1, self.__number_of_robots))
        robot_pos = self.__robots[catcher_robot].getField('translation').getSFVec3f()
        catcher_token = catcher_robot+'-TOKEN'
        token = self.__tokens[catcher_token]
        token.remove()
        self.__pop_token(catcher_token, type='Catcher', x=robot_pos[0], y=robot_pos[1])

    def __pop_token(self, token_name, type='Normal', x=0, y=0):
        self.__root_children.importMFNodeFromString(-1, 'DEF %s %s-Token2 { translation %s %s %s }'%(token_name, type, x, y, self.__token_z))
        self.__tokens[token_name] = self.getFromDef(token_name)

    def __pop_robot(self, controller=''):
        x = random.uniform(-1, 1)
        y = random.uniform(-0.65, 0.65)
        rotation = random.uniform(-math.pi, math.pi)
        robot_name = 'SEATECH-'+str(len(self.__robots)+1)

        if controller:
            controller = ', controller "%s"'%(controller)
        
        # With 'DEF' we can set Node definition
        self.__root_children.importMFNodeFromString(-1, 'DEF %s Seatech-E-puck { translation %s %s 0, rotation 0 0 1 %s, name "E-PUCK-%s" %s }'%(robot_name, x, y, rotation, robot_name, controller))
        
        token_name = robot_name+'-TOKEN'
        # With 'DEF' we can set Node definition
        self.__pop_token(token_name, x=x, y=y)

        robot = self.getFromDef(robot_name)
        recognition_field = robot.getProtoField('recognitionColors')
        # recognition_field.setSFColor(self.__hunter_color)
        print(recognition_field)
        self.__robots[robot_name] = robot

    def clear(self):
        for robot in self.__robots.values():
            robot.remove()
        self.__robots.clear()

        for token in self.__tokens.values():
            token.remove()
        self.__tokens.clear()

        self.__running = False

    def update_token_positions(self):
        for name, robot in self.__robots.items():
            pos = robot.getField('translation').getSFVec3f()
            self.__tokens[name+'-TOKEN'].getField('translation').setSFVec3f([pos[0], pos[1], self.__token_z])

    def check_catcher_collisions(self):
        # TODO : check if catcher touch someone
        pass

    def set_single_random_controller_mode(self):
        controller = self.__students_controllers[random.randrange(0,len(self.__students_controllers)-1)]
        print('\n>>>>> USING CONTROLLER %s\n'%(controller))
        self.__running = True
        for i in range(1, self.__number_of_robots):
            self.__pop_robot(controller=controller)
        self.__set_catcher()

    def set_all_controllers_mode(self):
        self.__running = True
        for controller in self.__students_controllers:
            self.__pop_robot(controller=controller)
        self.__set_catcher()
