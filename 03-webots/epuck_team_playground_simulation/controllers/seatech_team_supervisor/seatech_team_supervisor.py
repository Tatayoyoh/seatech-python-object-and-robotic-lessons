from controller import Supervisor

if __name__ == '__main__':
    TIME_STEP = 64
    supervisor = Supervisor()

    root_node = supervisor.getRoot()
    children_field = root_node.getField('children')
    # children_field.importMFNodeFromString(-1, 'Seatech-E-puck { translation 2.5 0 0.334, controller "seatech_epuck_controller" }')
    children_field.importMFNodeFromString(-1, 'Seatech-E-puck { translation 1 0 0 }')
    children_field.importMFNodeFromString(-1, 'Catcher-Token { translation 1 0 0.1 }')

    children_field.importMFNodeFromString(-1, 'Seatech-E-puck { translation 0.5 0 0 }')
    children_field.importMFNodeFromString(-1, 'Normal-Token { translation 0.5 0 0.1 }')

    children_field.importMFNodeFromString(-1, 'Seatech-E-puck { translation 1 1 0 }')
    children_field.importMFNodeFromString(-1, 'Normal-Token { translation 1 1 0.1 }')

    children_field.importMFNodeFromString(-1, 'Seatech-E-puck { translation 1 0.5 0 }')
    children_field.importMFNodeFromString(-1, 'Normal-Token { translation 1 0.5 0.1 }')

    children_field.importMFNodeFromString(-1, 'Seatech-E-puck { translation 0.5 0.5 0 }')
    children_field.importMFNodeFromString(-1, 'Normal-Token { translation 0.5 0.5 0.1 }')



    while supervisor.step(TIME_STEP) != -1:
        pass