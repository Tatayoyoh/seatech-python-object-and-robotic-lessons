class Singleton:
    __instance = None

    def __new__(cls,*args, **kwargs):
        if cls.__instance is None :
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

class Service1(Singleton):
    def great_action(self, text):
        print(f'Le texte passer en paramètre est {text}')
        
class Service2(Singleton):
    def great_action(self, text):
        print(f'Le texte passer en paramètre est {text}')
        
s11 = Service1()
s12 = Service1()
print(f's11==s12 ? {s11==s12 }')

s21 = Service2()
s22 = Service2()
print(f's21==s22 ? {s21==s22 }')

print(f's11==s22 ? {s11==s22 }')