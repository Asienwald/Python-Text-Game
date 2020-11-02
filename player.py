from random import randint
from items import *
from skills import *
from equipment import *
from quests import *

class player():
    data = []
    lvlup = False
    explefttolvlup = 0
    surplusexp = 0
    
    def __init__(self,name,scenecount,level,exp,money,dmg,defense,maxhp,currenthp,currentmana,
                 skillpts,skills,skilllvls,equipped,allequipment,equipweap,equiphead,equipbody,
                 equiphands,equiplegs,healingitems,healingitemscount,manaitems,manaitemscount,
                 quests,questprogress,completedquests):
        self.name = str(name)
        self.scenecount = int(scenecount)
        self.lvl = int(level)
        self.exp = int(exp)
        self.money = int(money)
        self.dmg = int(dmg)
        self.defense = int(defense)
        self.maxhp = int(maxhp)
        self.currenthp = int(currenthp)
        self.currentmana = int(currentmana)
        self.maxmana = 100
        self.skillpts = int(skillpts)
        self.skills = skills
        self.skilllvls = skilllvls
        self.equipped = equipped
        self.allequipment = allequipment
        self.equipweap = equipweap
        self.equiphead = equiphead
        self.equipbody = equipbody
        self.equiphands = equiphands
        self.equiplegs = equiplegs
        self.healingitems = healingitems
        self.healingitemscount = healingitemscount
        self.manaitems = manaitems
        self.manaitemscount = manaitemscount
        self.quests = quests
        self.questprogress = questprogress
        self.completedquests = completedquests
        self.killedmon = []

        self.alive = True
        if self.currenthp == self.maxhp: self.hpfull = True
        else: self.hpfull = False
        if self.currentmana == self.maxmana: self.manafull = True
        else: self.manafull = False

    def AcceptQuest(quest):
        self.quests += [quest]
        self.questprogress += [0]

    def EquipWeapon(self,weap):
        if self.lvl >= weap.lvl:
            self.dmg -= self.equipped[0].dmg
            self.equipped[0] = weap
            self.dmg += weap.dmg
            abitype = weap.specabitype
            abiamt = weap.specabiamt
            if abitype != None and abiamt != None:
                if abitype == "hp":
                    self.maxhp += abiamt
                elif abitype == "dmg":
                    self.dmg += abiamt
        else: print("Level too low!")

    def EquipArmor(self,armor):
        if self.lvl >= armor.lvl:
            abitype = armor.specabitype
            abiamt = armor.specabiamt
            if armor.cat == "head":
                self.defense -= self.equipped[1].defense
                self.equipped[1] = armor
            elif armor.cat == "body":
                self.defense -= self.equipped[2].defense
                self.equipped[2] = armor
            elif armor.cat == "hands":
                self.defense -= self.equipped[3].defense
                self.equipped[3] = armor
            elif armor.cat == "legs":
                self.defense -= self.equipped[4].defense
                self.equipped[4] = armor
            if abitype != None and abiamt != None:
                if abitype == "hp":
                    self.maxhp += abiamt
                elif abitype == "dmg":
                    self.dmg += abiamt
            self.defense += armor.defense
        else: print("Level too low!")

    def LvlSkill(self,skill):
        self.skillpts -= 1
        skillindex = self.skills.index(skill)
        self.skilllvls[skillindex] += 1
        skill.LvlSkill()

    def CheckItemCount(self):
        for i in self.healingitemscount:
            if i <= 0:
                healindex = self.healingitemscount.index(i)
                del self.healingitems[healindex]
                del self.healingitemscount[healindex]
        for i in self.manaitemscount:
            if i <= 0:
                manaindex = self.manaitemscount.index(i)
                del self.manaitems[manaindex]
                del self.manaitemscount[manaindex]

    def UseItem(self, item):
        if type(item) == healingitem:
            healindex = self.healingitems.index(item)
            self.healingitemscount[healindex] -= 1
            self.healhp(self.healingitems[healindex].healamt)
#            print("Used "+str(self.healingitemscount[healindex]))
        elif type(item) == manaitem:
            manaindex = self.manaitems.index(item)
            self.manaitemscount[manaindex] -= 1
            self.restoremana(self.manaitems[manaindex].restoreamt)
        self.CheckItemCount()

    def ThrowItem(self, item, throwamt):
        if type(item) == healingitem:
            healindex = self.healingitems.index(item)
            self.healingitemscount[healindex] -= throwamt
        elif type(item) == manaitem:
            manaindex = self.manaitems.index(item)
            self.manaitemscount[manaindex] -= throwamt
        self.CheckItemCount()

    def CheckIfHpFull(self):
        if self.currenthp >= self.maxhp:
            self.hpfull = True
        else:
            self.hpfull = False

    def healhp(self,healamt):
        self.currenthp += healamt
        if self.currenthp >= self.maxhp:
            self.currenthp = self.maxhp
#            self.hpfull = True
            print("Player hp is full!")
#        else:
#            self.hpfull = False
        self.CheckIfHpFull()

    def CheckIfManaFull(self):
        if self.currentmana >= self.maxmana:
            self.manafull = True
        else:
            self.manafull = False

    def restoremana(self,restoreamt):
        self.currentmana += restoreamt
        if self.currentmana >= self.maxmana:
            self.currentmana = self.maxmana
#            self.manafull = True
            print("Player mana is full!")
#        else:
#            self.manafull = False
        self.CheckIfManaFull()
    
    def atk(self):
        playerdealtdmg = randint(self.dmg - 2,self.dmg + 2)
        return playerdealtdmg

    def useSkill(self,skill):
        self.currentmana -= skill.manacost
        if type(skill) == DmgSkill:
            dealtdmg = randint(self.dmg - 2,self.dmg + 2)
            playerdealtdmg = dealtdmg * skill.dmgmultiplier
            return int(playerdealtdmg)
        elif type(skill) == HealSkill:
            self.healhp(skill.healamt)
#        print(self.currentmana)

    def lvledup(self):
#        global lvlup
        self.lvlup = True
        self.lvl += 1
        self.skillpts += 1
        self.maxhp += (self.lvl*10)
        self.currenthp = self.maxhp
        self.currentmana = self.maxmana
        self.dmg += self.lvl

    def getexp(self,amt):   #10
#        global lvlup,explefttolvlup,surplusexp
#        player.exp += amt
        self.explefttolvlup = (self.lvl*(10+self.lvl)) - self.surplusexp #11
        if amt >= self.explefttolvlup:    #10<11
            self.surplusexp = amt - self.explefttolvlup   #39
            self.exp += self.surplusexp  #39 exp
#            lvlup = True
            self.lvledup()
            self.explefttolvlup = (self.lvl*(10+self.lvl)) - self.surplusexp #24-39=-15
            while self.explefttolvlup < 0:
                self.lvledup()
                self.surplusexp -= (self.lvl*(10+self.lvl)) #39-39=0
                self.explefttolvlup = (self.lvl*(10+self.lvl)) - self.surplusexp
        else:
            self.exp += amt
            self.surplusexp += amt
            self.explefttolvlup = (self.lvl*(10+self.lvl)) - self.surplusexp
##        print(self.lvl)
##        print(explefttolvlup)
##        print(surplusexp)
        print(self.lvlup)

    def saveData(self):
        data = [self.name,self.scenecount,self.lvl,self.exp,self.money,
                self.dmg,self.defense,self.maxhp,self.currenthp,self.currentmana,self.skillpts]
        for i in self.skills:
            data += [i.name]
        for i in self.skilllvls:
            data += [i]
        count = 0
        for i in data:
            if type(i) != str:
                data[count] = str(i)
            if type(data[count]) == str:
                if (count + 1) == len(data):
                    None
                elif not data[count].endswith("\n"):
                    data[count] += "\n"
            count += 1
        print(data)
        with open("playerdata.txt","w") as playerdata:
            playerdata.writelines(data)

        dataequips = []
#        equipcount = 0
        for i in self.equipped:
            dataequips += [i.name+"\n"]
#            equipcount += 1
        dataequips += [".\n"]
#        equipcount += 1
        equipindex = dataequips.index(".\n")
        for i in self.allequipment[equipindex:]:
            dataequips += [i.name + "\n"]
        lastobj = dataequips[len(dataequips)-1]
        dataequips[len(dataequips)-1] = lastobj.replace("\n","")
        with open("playerequipment.txt","w") as playerequipment:
            playerequipment.writelines(dataequips)
        print(dataequips)

        dataitems = []
#        itemcount = 0
        for i in self.healingitems:
            dataitems += [i.name + "\n"]
#            itemcount += 1
        for i in self.manaitems:
            dataitems += [i.name + "\n"]
#            itemcount += 1
        for i in self.healingitemscount:
            dataitems += [str(i) + "\n"]
#            itemcount += 1
        for i in self.manaitemscount:
            dataitems += [str(i) + "\n"]
        lastobj = dataitems[len(dataitems)-1]
        dataitems[len(dataitems)-1] = lastobj.replace("\n","")
        with open("playeritems.txt","w") as playeritems:
            playeritems.writelines(dataitems)

        dataquests = []
        questtext = ""
        for i in self.quests:
            dataquests += [i.name + "\n"]
        for i in self.questprogress:
            dataquests += [str(i) + "\n"]
        for i in self.completedquests:
            questtext += i.name + ","
        dataquests += [questtext]
        with open("playerquests.txt","w") as playerquests:
            playerquests.writelines(dataquests)

    def takeDmg(self,amt):
        amt -= self.defense
        self.currenthp -= amt
        if self.currenthp <= 0:
            self.alive = False
            print("Player is dead!")

#dataSkills = []
dataskills = []
dataskillslvl = []
with open("playerdata.txt","r") as playerdata:
    data = playerdata.readlines()
    datacount = 0
    for i in data:
        if i.endswith("\n"):
            data[datacount] = i.replace("\n","")
        datacount += 1
    for yourskill in data[11:]:
        for i in allskills:
            if i.name == yourskill:
                dataskills += [i]
    for i in data[11+len(dataskills):]:
        dataskillslvl += [int(i)]
#                dataskillslvl += [yourskill]
##        if type(int(i)) == int:
##            dataskillslvl += [i]
##        elif type(i) == str:
##            dataSkills += [i]
##    print(data)
##    for yourskill in dataSkills:
##        for i in allskills:
##            if i.name == yourskill:
##                dataskills += [i]
#print(dataskills)

dataequipped = []
dataequipment = []
datanotequipped = []
dataweap = []
datahead = []
databody = []
datahands = []
datalegs = []
repeatedequips = []
with open("playerequipment.txt","r") as playerequipment:
    dataequips = playerequipment.readlines()
    equipindex = dataequips.index(".\n")
    for yourequip in dataequips:
        if yourequip.endswith("\n"):
            yourequip = yourequip.replace("\n","")
        for i in allequipment:
            if yourequip == i.name:
                dataequipment += [i]
    for i in dataequipment[:equipindex]:
        dataequipped += [i]
##    for i in dataequipment[equipindex:]:
##        datanotequipped += [i]
#    print(datanotequipped)
    for i in dataequipment:
        if type(i) == WeaponEquipment:
            dataweap += [i]
        elif type(i) == ArmorEquipment:
            if i.cat == "head":
                datahead += [i]
            elif i.cat == "body":
                databody += [i]
            elif i.cat == "hands":
                datahands += [i]
            elif i.cat == "legs":
                datalegs += [i]
        
datahealingitems = []
datahealingitemscount = []
datamanaitems = []
datamanaitemscount = []
with open("playeritems.txt","r") as playeritems:
    dataitems = playeritems.readlines()
    for youritem in dataitems:
        if youritem.endswith("\n"):
            youritem = youritem.replace("\n","")
        for i in healingitems:
            if i.name == youritem:
                datahealingitems += [i]
        for i in manaitems:
            if i.name == youritem:
                datamanaitems += [i]
    itemscount = len(datahealingitems) + len(datamanaitems)
    for i in dataitems[itemscount:itemscount+len(datahealingitems)]:
        datahealingitemscount += [int(i)]
    for i in dataitems[itemscount+len(datahealingitems):]:
        datamanaitemscount += [int(i)]

datacurrentquests = []
dataquestprogress = []
datacompletedquests = []
with open("playerquests.txt","r") as playerquests:
    dataquests = playerquests.readlines()
    print(dataquests)
    for yourquest in dataquests:
        if yourquest.endswith("\n"):
            yourquest = yourquest.replace("\n","")
        for i in allquests:
            if i.name == yourquest:
                datacurrentquests += [i]
    for i in dataquests[len(datacurrentquests):-1]:
        dataquestprogress += [int(i)]
    completedquests = dataquests[-1].split(",")
    for completed in completedquests:
        for i in allquests:
            if completed == "":
                None
            elif i.name == completed:
                datacompletedquests += [i]
                index = allquests.index(i)
                del allquests[index]
#print(datacompletedquests)
##print(datacurrentquests)
##print(dataquestprogress)
##print(allquests)

player = player(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],
                data[9],data[10],dataskills,dataskillslvl,dataequipped,dataequipment,
                dataweap,datahead,databody,datahands,datalegs,datahealingitems,
                datahealingitemscount,datamanaitems,datamanaitemscount,datacurrentquests,
                dataquestprogress,datacompletedquests)
player.EquipWeapon(player.equipped[0])
player.dmg += player.equipped[0].dmg
for i in player.equipped[1:]:
    player.defense += i.defense
    player.EquipArmor(i)

#player.saveData()
print(vars(player))
