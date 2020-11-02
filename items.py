#from player import *
import time

class Item():
    def __init__(self,name,descrip,buyprice,sellprice):
        self.name = name
        self.descrip = descrip
        self.buyprice = int(buyprice)
        self.sellprice = int(sellprice)

class healingitem(Item):
    def __init__(self,name,descrip,healamt,buyprice,sellprice):
        Item.__init__(self,name,descrip,buyprice,sellprice)
        healingitem.healamt = int(healamt)

class manaitem(Item):
    def __init__(self,name,descrip,restoreamt,buyprice,sellprice):
        Item.__init__(self,name,descrip,buyprice,sellprice)
        manaitem.restoreamt = int(restoreamt)

milk = healingitem("Milk","Freshly squeezed.\n Heals 5 HP.",20,2,1)
bread = healingitem("Bread","Just baked.\n Heals 10 HP.",10,5,2)
healingitems = [milk,bread]
#print(type(milk) == healingitem)

energycrystal = manaitem("Energy Crystal","Glows purple.\n Restores 10 mana.",10,10,5)
herb = manaitem("Herb","Can be found deep in Manerva's Cavern.\n Restores 10 mana.",10,10,5)
manaitems = [energycrystal,herb]
##print(milk.descrip)
##print(milk.healamt)
