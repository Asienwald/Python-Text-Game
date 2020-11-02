from monsters import *
from items import *

class Quest():
    def __init__(self,name,descrip,lvl,exp,money,completed):
        self.name = name
        self.descrip = descrip
        self.lvl = int(lvl)
        self.exp = int(exp)
        self.money = int(money)
        self.completed = bool(completed)

class KillQuest(Quest):
    def __init__(self,name,descrip,lvl,monstertokill,amttokill,killcount,exp,money,completed):
        Quest.__init__(self,name,descrip,lvl,exp,money,completed)
        self.monstertokill = monstertokill
        self.amttokill = int(amttokill)
        self.killcount = int(killcount)

class FindQuest(Quest):
    def __init__(self,name,descrip,lvl,itemtofind,amttofind,findcount,exp,money,completed):
        Quest.__init__(self,name,descrip,lvl,exp,money,completed)
        self.itemtofind = itemtofind
        self.amttofind = int(amttofind)
        self.findcount = int(findcount)

killwolves = KillQuest("Kill Wolves","Wolves are hunting on the villagers.\nKill them.",
                     1,wolf,10,0,100,40,False)
findherbs = FindQuest("Find Herbs","Help the girl find herbs for her sick brother.",
                      1,herb,1,0,200,50,False)
killslimes = KillQuest("Kill Slimes","Slimes have been pedoing on young girls in Altan.\nK I L L.",
                       1,slime,10,0,100,40,False)
allquests = [killwolves,findherbs,killslimes]

