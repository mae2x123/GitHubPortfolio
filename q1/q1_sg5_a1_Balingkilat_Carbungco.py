#Heroes
class Hero:
    def __init__(self,name,hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self,amount):
        self.hp -= amount
myHero = Hero("Arthur")
myHero2 = Hero("Morgana")
myHero.take_damage(10)
print("Arhtur's HP from 100 is", myHero.hp)
print("Morgana's HP from 100 is", myHero2.hp)
