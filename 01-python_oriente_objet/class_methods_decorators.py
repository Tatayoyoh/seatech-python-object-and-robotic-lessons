class Robot:
    __name = 'Simple Robot'
    __payloads = ['camera']
    
    def __init__(self, name, payloads=[]):
        self.__name = name
        self.__payloads = self.__payloads + payloads
  
    # getter
    @property
    def name(self):
        return self.__name
    @property
    def payloads(self):
        return self.__payloads

    @classmethod
    def get_original_name(cls):
        return cls.__name

    @classmethod
    def get_original_payloads(cls):
        return cls.__payloads

    @classmethod
    def war_robot(cls, name):
        return cls(name, ['gun', 'rockets', 'shield'])

    @classmethod
    def peace_robot(cls, name):
        return cls(name, ['flowers', 'rainbow', 'marijuana'])

    @staticmethod
    def calculate(arg1, arg2):
        print('La réponse est %s'%(arg1+arg2))

# static method call
Robot.calculate(20,22)

# normal object creation
r = Robot('Roger le robot', ['v8', 'joke generator'])
print(r.name, r.payloads)

# call class methods
print(r.get_original_name(), r.get_original_payloads())

# generate new robots from class methods
r = Robot.war_robot('Terminator')
print(r.name, r.payloads)

r = Robot.peace_robot('Hippinator')
print(r.name, r.payloads)


