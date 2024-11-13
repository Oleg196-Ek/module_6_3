import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0,0,0]
        self.speed = speed
    def move(self, dx, dy, dz):
        if sum (self._cords) + dz < 0:
            print("It's too deep, i can't dive :(" )
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        print (f'{self._cords[0]},{self._cords[1]}, {self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER <5:
            print(f'Sorry, i`m peaceful :)')

        else:
            print (f'Be careful, i`m attacking you 0_0')
class Bird(Animal):
    beak = True
    def __init__(self,speed):
        super().__init__(speed)
    def lay_eggs(self):
        number = random.randint(1,4)
        print(f'Here are(is) {number} eggs for you')
class AquaticAnimal (Animal):
    _DEGREE_OF_DANGER = 3
    def __init__(self,speed):
        super().__init__(speed)
    def dive_in(self, dz):
        dz = abs(dz)
        new_dz = self._cords[2] - (dz/2) * self.speed
        if new_dz < 0:
            print("It's too deep, i can't dive :(" )
        else:
            self._cords[2] = new_dz
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    def __init__(self, speed):
        super().__init__(speed)
class Duckbill ( Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        Bird.__init__(self,speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
    def speak(self):
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




