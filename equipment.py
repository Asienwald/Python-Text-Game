from items import *

class Equipment(Item):
    def __init__(self,name,descrip,level,specabitype,specabiamt,buyprice,sellprice):
        Item.__init__(self,name,descrip,buyprice,sellprice)
        self.lvl = int(level)
        if specabitype != None and specabiamt != None:
            self.specabitype = specabitype
            self.specabiamt = int(specabiamt)
        else:
            self.specabitype = None
            self.specabiamt = None

class WeaponEquipment(Equipment):
    def __init__(self,name,descrip,level,dmg,specabitype,specabiamt,buyprice,sellprice):
        Equipment.__init__(self,name,descrip,level,specabitype,specabiamt,buyprice,sellprice)
        self.dmg = int(dmg)

class ArmorEquipment(Equipment):
    def __init__(self,name,cat,descrip,level,defense,specabitype,specabiamt,buyprice,sellprice):
        Equipment.__init__(self,name,descrip,level,specabitype,specabiamt,buyprice,sellprice)
        self.cat = cat
        self.defense = int(defense)

#Starter Set
basicsword = WeaponEquipment("Basic Sword","Starter Weapon",1,10,None,None,1,1)
basichelmet = ArmorEquipment("Basic Helmet","head","Starter Armor",1,8,None,None,1,1)
basicarmor = ArmorEquipment("Basic Armor","body","Starter Armor",1,10,None,None,1,1)
basicgreaves = ArmorEquipment("Basic Greaves","hands","Starter Armor",1,5,None,None,1,1)
basicleggings = ArmorEquipment("Basic Leggings","legs","Starter Armor",1,5,None,None,1,1)
#Guard Set
sharpsword = WeaponEquipment("Sharp Sword","Just Sharpened. Effective against monsters",2,12,None,None,2,2)
guardhelm = ArmorEquipment("Guard Helmet","head","Armor worn by the Altan Guard Association",2,10,None,None,2,2)
guardarm = ArmorEquipment("Guard Armor","body","Armor worn by the Altan Guard Association",2,12,None,None,2,2)
guardgreaves = ArmorEquipment("Guard Greaves","hands","Armor worn by the Altan Guard Association",2,7,None,None,2,2)
guardleggings = ArmorEquipment("Guard Leggings","legs","Armor worn by the Altan Guard Association",2,7,None,None,2,2)

allequipment = [basicsword,basichelmet,basicarmor,basicgreaves,basicleggings,sharpsword,guardhelm,guardarm,
                guardgreaves,guardleggings]
#print(basicarmor.cat)
