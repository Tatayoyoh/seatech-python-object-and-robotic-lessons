class Robot():
    # Robot class content here
    pass

class Human():
    # Human class content here
    pass

class Cyborg(Robot, Human):
    # Cyborg class content here
    pass

cyb = Cyborg()

if issubclass(Cyborg, Human):
    print("Cyborg est une sous classe de Human!")

if issubclass(Cyborg, Robot):
    print("Cyborg est une sous classe de Robot !")

if isinstance(cyb, Human):
    print("Wesh frère t'es un mec un vrai !")

if isinstance(cyb, Robot):
    print("010110100101 101010100001 01010101110 !")