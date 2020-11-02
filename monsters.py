from random import randint

class monster():
    def __init__(self, name, level, hp, dmg):
        self.name = name
        self.lvl = level
        self.hp = hp
        self.dmg = dmg

    def atk(self):
        playertakendmg = randint(self.dmg-2,self.dmg+2)
        return playertakendmg

    def takeDmg(self,takenDmg):
        self.hp -= takenDmg

wolf = monster("Wolf",1,70,40)
hound = monster("Hound",1,60,50)
slime = monster("Slime",1,90,40)
lvl1 = [wolf,hound,slime]

goblin = monster("Goblin",2,70,50)
orc = monster("Orc",2,80,40)
bear = monster("Bear",2,80,50)
lvl2 = [goblin,orc,bear]

lvlmonsters = [lvl1, lvl2]
