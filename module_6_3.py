import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self):
        self._cords = [0,0,0]
        self.speed = 0
    def move(self, dx, dy, dz):
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed
        if z < 0:
            print("It's too deep, i can't dive :(" )
        else:
            self._cords = [x, y, z]

    def get_cords(self):
        print (f'{self._cords[0]},{self._cords[1]}, {self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER <5:
            print(f'Sorry, i`m peaceful :)')
        else:
            print (f'Be careful, i`m attacking you 0_0')
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        number = random.randint(1,4)
        print(f'Here are(is) {number} eggs for you')
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dive_z = abs(dz) // 2 * self.speed
        self._cords[2] -= dive_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill ( Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__()
        self.speed = speed

    def speak(self):
        if self.sound is not None:
            print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()




