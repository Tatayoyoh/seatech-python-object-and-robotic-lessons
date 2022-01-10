class Robot():
  """ My robot is awesome """
  name = 'Wall.E'
  def action(self):
    print('ACTION !')

def is_private(element):
    return element.startswith('__')

def collect_class_data(class_definition):
    methods = {'private':[], 'public':[]}
    attributes = {'private':[], 'public':[]}
    for element in dir(class_definition):
        privacy = 'private' if is_private(element) else 'public'
        if callable(getattr(Robot, element)):
            methods[privacy].append(element)
        else:
            attributes[privacy].append(element)

    return attributes, methods

if __name__ == '__main__':
    r = Robot()

    # Pour comparer votre objet
    isinstance(r, Robot)

    # Récupérer la valeur d'un attribut
    getattr(Robot, 'name')

    # Pour comparer votre objet
    callable(Robot().action)

    callable(Robot().action())

    dir(Robot)

    # Avec plus d'infos
    from pprint import pprint
    import inspect
    pprint(inspect.getmembers(Robot))
    
    attributes, methods = collect_class_data(Robot)
    print("\n\n# Home made display\n")
    print('methods')
    pprint(methods)
    print()
    print('attributes')
    pprint(attributes)


