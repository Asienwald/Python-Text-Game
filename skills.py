class Skill():
    def __init__(self,name,level,descrip,manacost):
        self.name = name
        self.lvl = int(level)
        self.descrip = descrip
        self.manacost = int(manacost)

class DmgSkill(Skill):
    def __init__(self,name,level,descrip,dmgmultiplier,manacost):
        Skill.__init__(self,name,level,descrip,manacost)
        self.dmgmultiplier = float(dmgmultiplier)

    def LvlSkill(self):
        self.dmgmultiplier += 0.5
        self.manacost += 5        

class HealSkill(Skill):
    def __init__(self,name,level,descrip,healamt,manacost):
        Skill.__init__(self,name,level,descrip,manacost)
        self.healamt = int(healamt)

    def LvlSkill(self):
        self.healamt += 10
        self.manacost += 5

thunderbolt = DmgSkill("Thunderbolt",1,"Summon lightning",2,10)
miniheal = HealSkill("Mini Heal",1,"Heal yourself",20,10)
allskills=[thunderbolt,miniheal]
#print(thunderbolt.name)
#print(miniheal.healamt)
