from controller import Supervisor

if __name__ == '__main__':
    TIME_STEP = 64
    supervisor = Supervisor()

    root_node = supervisor.getRoot()
    children_field = root_node.getField('children')
    children_field.importMFNodeFromString(4, 'DEF Seatech-E-puck Robot { controller "seatech_epuck_controller" }')

    while supervisor.step(TIME_STEP) != -1:
        pass