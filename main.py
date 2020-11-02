from tkinter import *
from tkinter import ttk
from random import randint
from STGVar import *
from monsters import *
from player import *
from items import *
from textartvar import *
import time
root = Tk()
root.config(bg="grey")
##style = ttk.Style()
##style.theme_use("clam")
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

font = "Aharoni 12 bold"          #init font

pdata = []      #name,scenecount,level,money,dmg,hp,items (all in str)
skillstext = ""
scenecount = 0

inputop = False #dialogue and scenes
userinput = ""

yourturn = False    #battle
battlefinished = True

def checkIfPlayerDead():
    if player.alive == False:
        addAction(actionview, "Your dead!")
        time.sleep(5)
        root.destroy()

def decreaseHp(amt):
##    global pdata
##    php = int(pdata[5])
##    php -= amt
##    pdata[5] = str(php)
    player.takeDmg(amt)
    addAction(actionview, "HP decreased by " + str(amt) + ".")
    addAction(actionview, str(player.currenthp) + " HP left.")

##def loadGame():
##    global pdata,name,scenecount,level,money,dmg,hp,items
##    datacount = 0
##    with open("playerdata.txt","r") as playerdata:
##        data = playerdata.readlines()
##        for i in data:
##            pdata += [i]
##loadGame()
##print(pdata)

##def saveGame():
##    count = 0
##    for i in pdata:
##        if type(i) != str:
##            pdata[count] = str(i) + "\n"
##        count += 1
##    with open("playerdata.txt","w") as playerdata:
##        playerdata.writelines(pdata)
##    print(pdata)

def SetDialogueText(Text, str):
    Text.config(state=NORMAL)
    Text.delete(0.0, END)       #totally delete text
    Text.insert(END, str)
    Text.config(state=DISABLED)

def addAction(Text, str):
    Text.config(state=NORMAL)      #totally delete text
    Text.insert(0.0, str + "\n")
    Text.config(state=DISABLED)

def setSkillsText():
    count = 1
    global skillstext
    itemstext = ""
    for i in player.skills:
        skillstext += str(count) + ". " + str(i) + "\n"
        count += 1

def openQuestMenu():
    quest = Toplevel(root)
    quest.title("Quests Menu")
    quest.geometry("500x400")
    quest.resizable(0,0)

    yourquestslabel = Label(quest,text="Your Quests: ",font=font,fg="blue")
    yourquestslabel.pack()
    yourquestslabel.place(x=20,y=20)

    questlistbox = Listbox(quest,width=30,height=18,font=font)
    questlistbox.pack()
    questlistbox.place(x=20,y=50)

    questdescriplabel = Label(quest,text="Quest Details: ",font=font,fg="blue")
    questdescriplabel.pack()
    questdescriplabel.place(x=250,y=20)
    
    questdescriptext = Text(quest,width=30,height=15,font=font,state=DISABLED)
    questdescriptext.pack()
    questdescriptext.place(x=250,y=50)

    def UpdateQuestListbox():
        questlistbox.delete(0,END)
        questcount = 1
        for i in player.quests:
            questlistbox.insert(END,str(questcount)+". "+i.name+" (Lv."+str(i.lvl)+")")
            questcount += 1
    UpdateQuestListbox()

    def UpdateQuestDescrip(quest):
        questdescriptext.config(state=NORMAL)
        questdescriptext.delete(0.0,END)
        if type(quest) == KillQuest:
            questdescriptext.config(fg="red")
            text = quest.descrip+"\n\n"+quest.monstertokill.name+" "+str(quest.killcount)+" / "+str(quest.amttokill)+"\n\nEXP: "+str(quest.exp)+"\nReward: "+str(quest.money)+"P"
        elif type(quest) == FindQuest:
            questdescriptext.config(fg="blue")
            text = quest.descrip+"\n\n"+quest.itemtofind.name+" "+str(quest.findcount)+" / "+str(quest.amttofind)+"\n\nEXP: "+str(quest.exp)+"\nReward: "+str(quest.money)+"P"
        questdescriptext.insert(END,text)
        questdescriptext.config(state=DISABLED)

    def QuestSelected(event):
        w = event.widget
        questindex = int(w.curselection()[0])

        UpdateQuestDescrip(player.quests[questindex])
    questlistbox.bind("<<ListboxSelect>>",QuestSelected)

def openEquipmentMenu():
    equip = Toplevel(root)
    equip.title("Equipment Menu")
    equip.geometry("600x500")
    equip.resizable(0,0)

##    def getNamesOfEquips(equiptype):
##        equipnames = []
##        for i in equiptype:
##            equipnames += [i.name]
##        return equipnames

    weaponlabel = Label(equip,text="Weapon: ",font=font,fg="blue")
    weaponlabel.pack()
    weaponlabel.place(x=20,y=20)
    weaplistbox = Listbox(equip,width=30,height=5,font=font)
    weaplistbox.pack()
    weaplistbox.place(x=20,y=50)
    weaplistbox.tag = "weap"

    headlabel = Label(equip,text="Head: ",font=font,fg="blue")
    headlabel.pack()
    headlabel.place(x=320,y=20)
    headlistbox = Listbox(equip,width=30,height=5,font=font)
    headlistbox.pack()
    headlistbox.place(x=320,y=50)
    headlistbox.tag = "head"

    bodylabel = Label(equip,text="Body: ",font=font,fg="blue")
    bodylabel.pack()
    bodylabel.place(x=20,y=160)
    bodylistbox = Listbox(equip,width=30,height=5,font=font)
    bodylistbox.pack()
    bodylistbox.place(x=20,y=190)
    bodylistbox.tag = "body"

    handslabel = Label(equip,text="Hands: ",font=font,fg="blue")
    handslabel.pack()
    handslabel.place(x=320,y=160)
    handslistbox = Listbox(equip,width=30,height=5,font=font)
    handslistbox.pack()
    handslistbox.place(x=320,y=190)
    handslistbox.tag = "hands"

    legslabel = Label(equip,text="Legs: ",font=font,fg="blue")
    legslabel.pack()
    legslabel.place(x=20,y=320)
    legslistbox = Listbox(equip,width=30,height=5,font=font)
    legslistbox.pack()
    legslistbox.place(x=20,y=350)
    legslistbox.tag = "legs"  

    equipdescriplabel = Label(equip,text="Equipment Description: ",font=font,fg="red")
    equipdescriplabel.pack()
    equipdescriplabel.place(x=320,y=320)
    equipdescriptext = Text(equip,height=7,width=30,state=DISABLED)
    equipdescriptext.pack()
    equipdescriptext.place(x=320,y=350)

    def UpdateEquipDescrip(text):
        equipdescriptext.config(state=NORMAL)
        equipdescriptext.delete(0.0,END)
        equipdescriptext.insert(END,text)
        equipdescriptext.config(state=DISABLED)

    def EquipSelected(event):
        w = event.widget
        equipindex = int(w.curselection()[0])
        equiptag = w.tag

        def getSpecAbi(equip):
            if equip.specabitype != None and equip.specabiamt != None:
                abitext = "\nSpecial Ability: "+equip.specabitype+"+"+str(specabiamt)
            else:
                abitext = "\nSpecial Ability: None"
            return abitext
        
        if equiptag == "weap":
            weap = player.equipweap[equipindex]
            dmgdiff = str(weap.dmg - player.equipped[0].dmg)
            abitext = getSpecAbi(weap)
            text = weap.descrip+"\nLv. "+str(weap.lvl)+"\nDMG: "+str(weap.dmg)+" ("+dmgdiff+")"+abitext+"\nSell Price: "+str(weap.sellprice)
        else:
            if equiptag == "head":
                arm = player.equiphead[equipindex]
                defdiff = str(arm.defense - player.equipped[1].defense)
            elif equiptag == "body":
                arm = player.equipbody[equipindex]
                defdiff = str(arm.defense - player.equipped[2].defense)
            elif equiptag == "hands":
                arm = player.equiphands[equipindex]
                defdiff = str(arm.defense - player.equipped[3].defense)
            elif equiptag == "legs":
                arm = player.equiplegs[equipindex]
                defdiff = str(arm.defense - player.equipped[4].defense)
            abitext = getSpecAbi(arm)
            text = arm.descrip+"\nLv. "+str(arm.lvl)+"\nDEF: "+str(arm.defense)+" ("+defdiff+")"+abitext+"\nSell Price: "+str(arm.sellprice)
        UpdateEquipDescrip(text)

        def Equip():
            if equiptag == "weap":
                weap = player.equipweap[equipindex]
                if player.lvl < weap.lvl: UpdateEquipDescrip("Level too low!")
                else: player.EquipWeapon(weap)
            else:
                if equiptag == "head":
                    arm = player.equiphead[equipindex]
                elif equiptag == "body":
                    arm = player.equipbody[equipindex]
                elif equiptag == "hands":
                    arm = player.equiphands[equipindex]
                elif equiptag == "legs":
                    arm = player.equiplegs[equipindex]
                if player.lvl < arm.lvl: UpdateEquipDescrip("Level too low!")
                else: player.EquipArmor(arm)
            UpdateListboxes()

        weaplistbox.bind("<Double-Button-1>",lambda x:Equip())
        headlistbox.bind("<Double-Button-1>",lambda x:Equip())
        bodylistbox.bind("<Double-Button-1>",lambda x:Equip())
        handslistbox.bind("<Double-Button-1>",lambda x:Equip())
        legslistbox.bind("<Double-Button-1>",lambda x:Equip())
            
    weaplistbox.bind("<<ListboxSelect>>",EquipSelected)
    headlistbox.bind("<<ListboxSelect>>",EquipSelected)
    bodylistbox.bind("<<ListboxSelect>>",EquipSelected)
    handslistbox.bind("<<ListboxSelect>>",EquipSelected)
    legslistbox.bind("<<ListboxSelect>>",EquipSelected)

    def UpdateListboxes():
#        weaplistbox.delete(0,END)

        def InsertEquips(equiplist,lb):
            lb.delete(0,END)
            count = 1
            for i in equiplist:
                if i in player.equipped:
                    lb.insert(END,str(count)+". "+i.name+" (Equipped)")
                else:
                    lb.insert(END,str(count)+". "+i.name)
                count += 1

        InsertEquips(player.equipweap,weaplistbox)
        InsertEquips(player.equiphead,headlistbox)
        InsertEquips(player.equipbody,bodylistbox)
        InsertEquips(player.equiphands,handslistbox)
        InsertEquips(player.equiplegs,legslistbox)

    UpdateListboxes()

def openSkillsMenu():
    skills = Toplevel(root)
    skills.title("Skills Menu")
    skills.geometry("400x400")
    skills.resizable(0,0)

    yourskillslabel = Label(skills,text="Your skills: ",font=font,fg="blue")
    yourskillslabel.pack()
    yourskillslabel.place(x=20,y=40)

    yourskillptslabel = Label(skills,text="Your skill points: "+str(player.skillpts),font=font,fg="red")
    yourskillptslabel.pack()
    yourskillptslabel.place(x=20,y=20)

    skillslistbox = Listbox(skills,height=8,width=40,font=font)
    skillslistbox.pack()
    skillslistbox.place(x=20,y=70)

    skillsdescriplabel = Label(skills,text="Skill Description: ",font=font,fg="blue")
    skillsdescriplabel.pack()
    skillsdescriplabel.place(x=20,y=250)
    skillsdescriptext = Text(skills,height=5,width=40,state=DISABLED,font=font)
    skillsdescriptext.pack()
    skillsdescriptext.place(x=20,y=280)

    def UpdateSkillPtsLabel():
        yourskillptslabel.config(text="Your skill points: "+str(player.skillpts))

    def UpdateSkillDescrip(skillindex):
        skillsdescriptext.config(state=NORMAL)
        skillsdescriptext.delete(0.0,END)
        skillsdescriptext.insert(END,player.skills[skillindex].descrip + "\n")
        skillsdescriptext.insert(END,"Manacost: "+str(player.skills[skillindex].manacost))
#        skillsdescriptext.insert(END,"\n"+str(player.skills[skillindex].manacost)) #
        skillsdescriptext.config(state=DISABLED)

    def UpdateSkillsListbox():
        skillslistbox.delete(0,END)
        skillcount = 0
        for i in player.skills:
            skillslistbox.insert(END,
                str(skillcount+1)+". "+player.skills[skillcount].name+"   (Lv."+str(player.skilllvls[skillcount])+")")
            skillcount += 1
    UpdateSkillsListbox()

    def SkillSelected(event):
        widget = event.widget
        skillindex = int(widget.curselection()[0])
        UpdateSkillDescrip(skillindex)
    
        def openSkillLvlUp():
            skilllvlup = Toplevel(skills)
            skilllvlup.title("Level Up Skill")
            skilllvlup.geometry("240x120")
            skilllvlup.resizable(0,0)

            skilllvluplabel = Label(skilllvlup,text="Level Skill Up?",font=font,fg="blue")
            skilllvluplabel.pack()
            skilllvluplabel.place(x=20,y=20)

            def lvlskill():
                player.LvlSkill(player.skills[skillindex])
                UpdateSkillsListbox()
                if player.skillpts <= 0:
                    skillslistbox.unbind("<Double-Button-1>")
                UpdateSkillPtsLabel()
                skilllvlup.destroy()

            yesbtn = Button(skilllvlup,text="Yes",font=font,fg="blue",width=6,
                            command=lvlskill)
            yesbtn.pack()
            yesbtn.place(x=135,y=65)

            nobtn = Button(skilllvlup,text="No",font=font,fg="red",width=6,
                           command=lambda:skilllvlup.destroy())
            nobtn.pack()
            nobtn.place(x=20,y=65)

        if player.skillpts > 0:
            skillslistbox.bind("<Double-Button-1>",lambda x:openSkillLvlUp())
            
    skillslistbox.bind("<<ListboxSelect>>",SkillSelected)
    
#    SkillLvlUp()
#openSkillsMenu()

def openInventory():
    inven = Toplevel(root)
    inven.title("Player Inventory")
    inven.geometry("500x500")
    inven.resizable(0,0)

    healitemslabel = Label(inven,text="Your Healing Items: ",font=font,fg="red")
    healitemslabel.pack()
    healitemslabel.place(relx=0.05,rely=0.04)
    healitemslistbox = Listbox(inven,height=8,width=30,font=font)
    healitemslistbox.pack()
    healitemslistbox.place(relx=0.05,rely=0.1)

    manaitemslabel = Label(inven,text="Your Mana Items: ",font=font,fg="blue")
    manaitemslabel.pack()
    manaitemslabel.place(relx=0.05,rely=0.49)
    manaitemslistbox = Listbox(inven,height=8,width=30,font=font)
    manaitemslistbox.pack()
    manaitemslistbox.place(relx=0.05,rely=0.55)

    descriplabel = Label(inven,text="Item Description: ",font=font)
    descriplabel.pack()
    descriplabel.place(relx=0.6,rely=0.04)
    descriptext = Text(inven,font=font,width=20,height=8,state=DISABLED)
    descriptext.pack()
    descriptext.place(relx=0.6,rely=0.1)

    itemsloglabel = Label(inven,text="Items Log: ",font=font)
    itemsloglabel.pack()
    itemsloglabel.place(relx=0.6,rely=0.49)
    itemslogtext = Text(inven,width=20,height=8,state=DISABLED)
    itemslogtext.pack()
    itemslogtext.place(relx=0.6,rely=0.55)

    instructionstext = """Double click on item to use.
Press <t> while selecting item to throw."""
    instructionslabel = Label(inven,text=instructionstext,fg="blue")
    instructionslabel.pack()
    instructionslabel.place(relx=0.3,rely=0.9)

    def UpdateItemLog(text):
        itemslogtext.config(state=NORMAL)
#        itemslogtext.delete(0.0,END)
        itemslogtext.insert(0.0,text+"\n")
        itemslogtext.config(state=DISABLED)

    def UpdateText(Text, str):
        Text.config(state=NORMAL)
        Text.delete(0.0,END)
        Text.insert(END,str)
        Text.config(state=DISABLED)

#    healindex = 0    
    def OnHealItemSelected(event):
        widget = event.widget
        healindex = int(widget.curselection()[0])
        UpdateText(descriptext,player.healingitems[healindex].descrip)

        def UseHealItem():
            openUseMenu(player.healingitems[healindex])
            UpdateHealListBox()

        def ThrowHealingItem(event):
            openThrowMenu(player.healingitems[healindex])
        
        healitemslistbox.bind("<Double-Button-1>",lambda x:UseHealItem())
        healitemslistbox.bind("<t>",ThrowHealingItem)
    healitemslistbox.bind("<<ListboxSelect>>",OnHealItemSelected)

    def OnManaItemSelected(event):
        widget = event.widget
        manaindex = int(widget.curselection()[0])
        UpdateText(descriptext,player.manaitems[manaindex].descrip)

        def UseManaItem():
            openUseMenu(player.manaitems[manaindex])
            UpdateManaListBox()

        def ThrowManaItem(event):
            openThrowMenu(player.manaitems[manaindex])

        manaitemslistbox.bind("<Double-Button-1>",lambda x:UseManaItem())
        manaitemslistbox.bind("<t>",ThrowManaItem)
    manaitemslistbox.bind("<<ListboxSelect>>",OnManaItemSelected)

    def openThrowMenu(item):
        throw = Toplevel(inven)
        throw.title("Throw Item")
        throw.geometry("200x150")

        throwamtlabel = Label(throw,text="Input amount to throw: ",font=font,fg="blue")
        throwamtlabel.pack()
        throwamtlabel.place(relx=0.1,rely=0.05)
        throwamttext = Text(throw,font=font,height=1,width=15)
        throwamttext.pack()
        throwamttext.place(relx=0.1,rely=0.25)

        def confirmThrow():
            throwamt = int(throwamttext.get(0.0,END))
            player.ThrowItem(item,throwamt)
            UpdateItemLog("You threw "+str(throwamt)+" "+str(item.name)+"!")
            UpdateHealListBox()
            UpdateManaListBox()
            throw.destroy()

        def cancelThrow():
            throw.destroy()

        throwbtn = Button(throw,text="Throw",font=font,fg="blue",command=confirmThrow)
        throwbtn.pack()
        throwbtn.place(relx=0.6,rely=0.6)

        cancelbtn = Button(throw,text="Cancel",font=font,fg="red",command=cancelThrow)
        cancelbtn.pack()
        cancelbtn.place(relx=0.1,rely=0.6)

    def openUseMenu(item):
        use = Toplevel(inven)
        use.title("Use Item")
        use.geometry("200x100")

        uselabel = Label(use,text="Use Item?",font=font,fg="blue")
        uselabel.pack()
        uselabel.place(relx=0.1,rely=0.1)
        
        nobtn = Button(use,text="No",font=font,fg="red",width=5,command=lambda:use.destroy())
        nobtn.pack()
        nobtn.place(relx=0.1,rely=0.45)

        def useItem():
            player.UseItem(item)
            UpdateItemLog("You used "+str(item.name)+"!")
            if type(item) == healingitem:
                UpdateItemLog(str(item.healamt)+" HP healed.")
                if player.hpfull == True:
                    UpdateItemLog("Full HP!")
            elif type(item) == manaitem:
                UpdateItemLog(str(item.restoreamt)+" Mana restored.")
                if player.manafull == True:
                    UpdateItemLog("Full Mana!")
            UpdateHealListBox()
            UpdateManaListBox()
            use.destroy()

        yesbtn = Button(use,text="Yes",font=font,fg="blue",width=5,command=lambda:useItem())
        yesbtn.pack()
        yesbtn.place(relx=0.6,rely=0.45)
    
    def UpdateHealListBox():
        healitemslistbox.delete(0,END)
        healcount = 1
        for i in player.healingitems:
            healtext = str(healcount)+". "+i.name+"     ("+str(player.healingitemscount[healcount-1])+")"
            healitemslistbox.insert(END, healtext)
            healcount += 1
    UpdateHealListBox()

    def UpdateManaListBox():
        manaitemslistbox.delete(0,END)
        manacount = 1
        for i in player.manaitems:
            manatext = str(manacount)+". "+i.name+"    ("+str(player.manaitemscount[manacount-1])+")"
            manaitemslistbox.insert(END, manatext)
            manacount += 1
    UpdateManaListBox()
            
def OpenMenu():   
    menu = Toplevel(root)
    menu.title("Player Menu")
    menu.geometry("300x450")
    menu.resizable(0,0)

    namelabel = Label(menu,fg="green", text="Name : "+player.name,font=font)
    namelabel.pack()
    namelabel.place(x=20,y=20)

    moneylabel = Label(menu,fg="green", text="Money : " + str(player.money),font=font)
    moneylabel.pack()
    moneylabel.place(x=20,y=50)

    lvllabel = Label(menu,fg="green", text="Lv: "+str(player.lvl),font=font)
    lvllabel.pack()
    lvllabel.place(x=20,y=80)

    dmglabel = Label(menu,fg="red", text="DMG: "+str(player.dmg),font=font)
    dmglabel.pack()
    dmglabel.place(x=20,y=110)

    deflabel = Label(menu,fg="red",text="DEF: "+str(player.defense),font=font)
    deflabel.pack()
    deflabel.place(x=20,y=140)

    hplabel = Label(menu,fg="blue", text="HP: "+str(player.currenthp)+" / "+str(player.maxhp),font=font)
    hplabel.pack()
    hplabel.place(x=20,y=170)

    manalabel = Label(menu,fg="blue",text="Mana: "+str(player.currentmana)+" / "+str(player.maxmana),font=font)
    manalabel.pack()
    manalabel.place(x=20,y=200)
    
    skillslabel = Label(menu, text="Your Skills : ",font=font)
    skillslabel.pack()
    skillslabel.place(x=20,y=230)
    
    setSkillsText()
    skillslist = Text(menu,height=8,width=28)
    skillslist.insert(END,skillstext)
    skillslist.pack()
    skillslist.place(x=20,y=270)

root.title("Simple Text Game")  #Set title of window
#root.attributes("-fullscreen", True)
root.state("zoomed")
##w, h = root.winfo_screenwidth(), root.winfo_screenheight()
##root.geometry("%dx%d+0+0" % (w, h))
#root.geometry("600x400")        #Set size of window
root.resizable(0,0)             #Set window unresizable

canvas = Canvas(root,height=500,width=900)
canvas.pack()
canvas.place(x=200,y=30)

afont = "Courier 8 bold"
def createText(x,y,text,color):
    canvas.create_text(x,y,text=text,fill=color,font=afont)
def animscene1():
#    canvas.config(background="#50FF61")
    createText(100,150,tree1,"green")
    createText(300,80,trees,"green")
    createText(700,120,trees,"green")
    createText(800,400,tree2,"green")
    createText(440,350,dirtpath,"brown")

animscene1()

dialogue = Text(root, height=8, width=70,font=font)#init dialogue text
dialogue.pack()                                    #creating text
##if player.scenecount == 1: SetDialogueText(dialogue,scenes[player.scenecount-1])
##else: SetDialogueText(dialogue,scenes[player.scenecount])
SetDialogueText(dialogue,scenes[player.scenecount])
dialogue.config(state=DISABLED)                    #make text read only
dialogue.place(x=140,y=570)    #setting pos of text

savebtn = Button(root,text="Save",width=10,height=2,command=player.saveData,font=font)
savebtn.pack()
savebtn.place(x=1200,y=20)

menubtn = Button(root, text="Menu",width=10,height=2,command=OpenMenu,font=font)
menubtn.pack()
menubtn.place(x=20,y=20)

equipbtn = Button(root,text="Equipment",width=10,height=2,command=openEquipmentMenu,font=font)
equipbtn.pack()
equipbtn.place(x=20,y=90)

invenbtn = Button(root,text="Inventory",width=10,height=2,command=openInventory,font=font)
invenbtn.pack()
invenbtn.place(x=20,y=160)

skillsbtn = Button(root,text="Skills",width=10,height=2,command=openSkillsMenu,font=font)
skillsbtn.pack()
skillsbtn.place(x=20,y=230)

questsbtn = Button(root,text="Quests",width=10,height=2,command=openQuestMenu,font=font)
questsbtn.pack()
questsbtn.place(x=20,y=300)

nextbtn = Button(root, text="Next",width=10,height=2,font=font)
nextbtn.config(command=lambda : nextScene(dialogue))
nextbtn.pack()
nextbtn.place(x=1150,y=500)

actionlabel = Label(root, text="Actions: ",font=font)
actionlabel.pack()
actionlabel.place(x=700,y=540)
actionview = Text(root, height=8,width=60)
actionview.pack()
actionview.config(state=DISABLED)
actionview.place(x=700,y=570)

##tasklabel = Label(root, text="Task: ",font=font)
##tasklabel.pack()
##tasklabel.place(relx=0.58,rely=0.63)
##taskview = Text(root,height=5,width=20)
##taskview.pack()
##taskview.config(state=DISABLED)
##taskview.place(relx=0.58,rely=0.7)

def receivedexp(amt):
    player.getexp(amt)
    addAction(actionview,"You got "+str(amt)+ " exp.")
    if player.lvlup == True:
        addAction(actionview,"You leveled up!")
        addAction(actionview,str(player.explefttolvlup)+" exp left to next level.")
        player.lvlup = False
    else:
        addAction(actionview,str(player.explefttolvlup)+" exp left to level up.")

def openBattle():
    global yourturn,battlefinished
    battlefinished = False
    alive = True
    moncount = randint(0,2)
#    print(player.lvl)
    lvlmonster = lvlmonsters[player.lvl-1]
    pickedmondetails = lvlmonster[moncount]
    pickedmon = pickedmondetails
    monsterdead = False
    player.alive = True
    
    battle = Toplevel(root)
    battle.title("You have encountered a monster!")
    battle.geometry("500x500+500+30")
    battle.resizable(0,0)

    monnamelabel = Label(battle,text=pickedmon.name,font=("Times",20))
    monnamelabel.pack()
    monnamelabel.place(relx=0.3,rely=0.05)

    monlvllabel = Label(battle,text="Lv. " + str(pickedmon.lvl),font=("Times",20))
    monlvllabel.pack()
    monlvllabel.place(relx=0.1,rely=0.05)

    monhplabel = Label(battle,text="Monster HP: " + str(pickedmon.hp),
                       font=("Times",16),fg="red")
    monhplabel.pack()
    monhplabel.place(relx=0.1,rely=0.15)

    yourhplabel = Label(battle,
                        text="Your HP: "+str(player.currenthp)+" / "+str(player.maxhp),
                        font=("Times",16,"bold"),fg="blue")
    yourhplabel.pack()
    yourhplabel.place(relx=0.1,rely=0.2)

    yourmanalabel = Label(battle,
                          text="Your Mana: "+str(player.currentmana)+" / "+str(player.maxmana),
                          font=("Times 16 bold"),fg="blue")
    yourmanalabel.pack()
    yourmanalabel.place(relx=0.1,rely=0.25)

    nextmovelabel = Label(battle,text="What's your move?",font=font)
    nextmovelabel.pack()
    nextmovelabel.place(relx=0.1,rely=0.3)

    battleloglabel = Label(battle,text="Battle Log: ",font=font)
    battleloglabel.pack()
    battleloglabel.place(relx=0.1,rely=0.68)
    battlelogtext = Text(battle,width=50,height=6,fg="blue",state=DISABLED)
    battlelogtext.pack()
    battlelogtext.place(relx=0.1,rely=0.75)

    atkbtn = Button(battle,text="Attack",width=10,height=5,font=font,bg="red",fg="white")
    atkbtn.config(command=lambda : playeratk())
    atkbtn.pack()
    atkbtn.place(relx=0.1,rely=0.4)

    def UpdateText(Text, str):
        Text.config(state=NORMAL)
        Text.delete(0.0,END)
        Text.insert(END,str)
        Text.config(state=DISABLED)

    def updateHpLabel():
        yourhplabel.config(text="Your HP: "+str(player.currenthp)+" / "+str(player.maxhp))

    def updateManaLabel():
        yourmanalabel.config(text="Your Mana: "+str(player.currentmana)+" / "+str(player.maxmana))

    def useSkillInBattle():
        useskill = Toplevel(battle)
        useskill.title("Use Skill In Battle")
        useskill.geometry("300x400")
        useskill.resizable(0,0)

        skillslabel = Label(useskill,text="Your Skills: ",font=font,fg="blue")
        skillslabel.pack()
        skillslabel.place(x=20,y=10)
        skillslistbox = Listbox(useskill,height=10,width=30,font=font)
        skillslistbox.pack()
        skillslistbox.place(x=20,y=40)

        skillsdescriplabel = Label(useskill,text="Skill Description: ",font=font,fg="blue")
        skillsdescriplabel.pack()
        skillsdescriplabel.place(x=20,y=250)
        skillsdescriptext = Text(useskill,height=5,width=30,state=DISABLED,font=font)
        skillsdescriptext.pack()
        skillsdescriptext.place(x=20,y=280)

        def UpdateSkillDescrip(skillindex):
            skillsdescriptext.config(state=NORMAL)
            skillsdescriptext.delete(0.0,END)
            skillsdescriptext.insert(END,player.skills[skillindex].descrip+"\n")
            skillsdescriptext.insert(END,"Manacost: "+str(player.skills[skillindex].manacost))
    #        skillsdescriptext.insert(END,"\n"+str(player.skills[skillindex].manacost)) #
            skillsdescriptext.config(state=DISABLED)

        def UpdateSkillsListbox():
            skillslistbox.delete(0,END)
            skillcount = 0
            for i in player.skills:
                skillslistbox.insert(END,
                    str(skillcount+1)+". "+player.skills[skillcount].name+"   (Lv."+str(player.skilllvls[skillcount])+")")
                skillcount += 1
        UpdateSkillsListbox()

        def SkillSelected(event):
            widget = event.widget
            skillindex = int(widget.curselection()[0])
            UpdateSkillDescrip(skillindex)

            def useSkill():
                skill = player.skills[skillindex]
                updatebattlelog("You used "+skill.name+".")
                if type(skill) == DmgSkill:
                    playerdealtdmg = player.useSkill(player.skills[skillindex])
                    pickedmon.takeDmg(playerdealtdmg)
                    updatemonhplabel()
#                    updateyourmanalabel()
                    updatebattlelog("You dealt "+str(playerdealtdmg)+" dmg to "+pickedmon.name+"!")
                elif type(skill) == HealSkill:
                    player.useSkill(skill)
                    updateyourhplabel()
                    updatebattlelog("You healed "+str(skill.healamt)+" HP.")
##                    print(player.currentmana)
##                    print(skill.manacost)
                updateyourmanalabel()
                checkmonsterdead()
                useskill.destroy()
            skillslistbox.bind("<Double-Button-1>",lambda x:useSkill())                
                
        skillslistbox.bind("<<ListboxSelect>>",SkillSelected)
#    useSkillInBattle()

    def useItemInBattle():
        usebattle = Toplevel(battle)
        usebattle.title("Use Item In Battle")
        usebattle.geometry("300x550")
        usebattle.resizable(0,0)

        healitemslabel = Label(usebattle,text="Your Healing Items: ",font=font,fg="red")
        healitemslabel.pack()
        healitemslabel.place(relx=0.05,rely=0.02)
        healitemslistbox = Listbox(usebattle,height=8,width=30,font=font)
        healitemslistbox.pack()
        healitemslistbox.place(relx=0.05,rely=0.07)

        manaitemslabel = Label(usebattle,text="Your Mana Items: ",font=font,fg="blue")
        manaitemslabel.pack()
        manaitemslabel.place(relx=0.05,rely=0.4)
        manaitemslistbox = Listbox(usebattle,height=8,width=30,font=font)
        manaitemslistbox.pack()
        manaitemslistbox.place(relx=0.05,rely=0.45)

        descriplabel = Label(usebattle,text="Items Description: ",font=font)
        descriplabel.pack()
        descriplabel.place(relx=0.05,rely=0.76)
        descriptext = Text(usebattle,width=30,height=5,state=DISABLED)
        descriptext.pack()
        descriptext.place(relx=0.05,rely=0.82)

        def UpdateHealListBox():
            healitemslistbox.delete(0,END)
            healcount = 1
            for i in player.healingitems:
                healtext = str(healcount)+". "+i.name+"     ("+str(player.healingitemscount[healcount-1])+")"
                healitemslistbox.insert(END, healtext)
                healcount += 1
        UpdateHealListBox()

        def UpdateManaListBox():
            manaitemslistbox.delete(0,END)
            manacount = 1
            for i in player.manaitems:
                manatext = str(manacount)+". "+i.name+"    ("+str(player.manaitemscount[manacount-1])+")"
                manaitemslistbox.insert(END, manatext)
                manacount += 1
        UpdateManaListBox()

        def OnHealItemSelected(event):
            widget = event.widget
            healindex = int(widget.curselection()[0])
            UpdateText(descriptext,player.healingitems[healindex].descrip)

            def UseHealItem():
#                openUseMenu(player.healingitems[healindex])
                updatebattlelog(str(player.healingitems[healindex].healamt)+" HP healed.")
                player.UseItem(player.healingitems[healindex])
                updateHpLabel()
                updatebattlelog("Waiting for enemy move...")
                battle.after(2000,monsteratk)
                usebattle.destroy()
#                UpdateHealListBox()

##           def ThrowHealingItem(event):
##                openThrowMenu(player.healingitems[healindex])
        
            healitemslistbox.bind("<Double-Button-1>",lambda x:UseHealItem())
#            healitemslistbox.bind("<t>",ThrowHealingItem)
        healitemslistbox.bind("<<ListboxSelect>>",OnHealItemSelected)

        def OnManaItemSelected(event):
            widget = event.widget
            manaindex = int(widget.curselection()[0])
            UpdateText(descriptext,player.manaitems[manaindex].descrip)

            def UseManaItem():
#                openUseMenu(player.manaitems[manaindex])
                updatebattlelog(str(player.manaitems[manaindex].restoreamt)+" Mana restored.")
                player.UseItem(player.manaitems[manaindex])
                updateManaLabel()
                updatebattlelog("Waiting for enemy move...")
                battle.after(2000,monsteratk)
                usebattle.destroy()
#                UpdateManaListBox()

##            def ThrowManaItem(event):
##                openThrowMenu(player.manaitems[manaindex])

            manaitemslistbox.bind("<Double-Button-1>",lambda x:UseManaItem())
#        manaitemslistbox.bind("<t>",ThrowManaItem)
        manaitemslistbox.bind("<<ListboxSelect>>",OnManaItemSelected)

    useitembtn = Button(battle,text="Use Item",width=10,height=5,font=font,bg="red",
                        fg="white",command=lambda:useItemInBattle())
    useitembtn.pack()
    useitembtn.place(relx=0.4,rely=0.4)

    castbtn = Button(battle,text="Cast Spell",width=10,height=5,font=font,
                     bg="red",fg="white",command=lambda:useSkillInBattle())
    castbtn.pack()
    castbtn.place(relx=0.7,rely=0.4)       
    
    def updatebattlelog(string):
        battlelogtext.config(state=NORMAL)
        battlelogtext.insert(0.0,string+"\n")
        battlelogtext.config(state=DISABLED)

    def updatemonhplabel():
        monhplabel.config(text="HP: "+str(pickedmon.hp))

    def updateyourhplabel():
        yourhplabel.config(text="Your HP: "+str(player.currenthp)+" / "+str(player.maxhp))

    def updateyourmanalabel():
        yourmanalabel.config(text="Your Mana: "+str(player.currentmana)+" / "+str(player.maxmana))
           
    def monsteratk():
        playertakendmg = pickedmon.atk()
        player.takeDmg(playertakendmg)
        checkIfPlayerDead()
        updateyourhplabel()
##        addAction(battlelogtext,pickedmon.name+" dealt "+str(playertakendmg)+" dmg to "
##                  +player.name+"!")
##        addAction(battlelogtext,player.name+" has "+str(player.hp)+" HP left!")
        updatebattlelog(pickedmon.name+" dealt "+str(playertakendmg)+" dmg to "
                  +player.name+"!")
        updatebattlelog(player.name+" has "+str(player.currenthp)+" HP left!")
#        yourturn = True

    def playeratk():
        global yourturn
        playerdealtdmg = player.atk()
        pickedmon.hp -= playerdealtdmg
##        addAction(battlelogtext,pickedmon.name+" received "+str(playerdealtdmg)+
##                  " dmg from "+player.name+"!")
#        updatebattlelog(pickedmon.name+" received "+str(playerdealtdmg)+
#                  " dmg from "+player.name+"!")
        updatebattlelog("You dealt "+str(playerdealtdmg)+" dmg to "+pickedmon.name+"!")
        updatemonhplabel()
        yourturn = False
        checkmonsterdead()

    def checkmonsterdead():
        if pickedmon.hp <= 0:
            pickedmon.hp = 0
            updatemonhplabel()
            addAction(battlelogtext,player.name+" killed "+pickedmon.name)
            atkbtn.config(state=DISABLED)
            useitembtn.config(state=DISABLED)
            castbtn.config(state=DISABLED)
            battlefinished = True
            nextbtn.config(state=ACTIVE)
##            player.getexp(pickedmon.lvl*10)
##            addAction(actionview,"lmao")
            receivedexp(pickedmon.lvl*10+1)
            battle.after(3000,battle.destroy)
        else:
#            monsteratk()
            disableButtons()
            battle.after(2000,monsteratk)
            battle.after(2000,setYourTurn)

    def disableButtons():
        atkbtn.config(state=DISABLED)
        useitembtn.config(state=DISABLED)
        castbtn.config(state=DISABLED)

    whohitfirst = randint(1,2)
    if whohitfirst == 1: yourturn = True; updatebattlelog("You start first!"); disableButtons()
    else: turntext = yourturn = False; updatebattlelog("The enemy starts first!")

    def setYourTurn():
        yourturn = True
        atkbtn.config(state=ACTIVE)
        useitembtn.config(state=ACTIVE)
        castbtn.config(state=ACTIVE)

    if not yourturn:
        disableButtons()
        battle.after(2000,monsteratk)
        battle.after(2000,setYourTurn)
#        yourturn = True
    if yourturn:
        atkbtn.config(state=ACTIVE)
        useitembtn.config(state=ACTIVE)
        castbtn.config(state=ACTIVE)

    def onClosing():
        print("Tried to escape? Try again.")
#        None

    battle.protocol("WM_DELETE_WINDOW", onClosing)

def scenemanager(Text):
    global inputop
    if player.scenecount == 1 and inputop == False:     #if at scene2 which has options and havent selected op
        nextbtn.config(state=DISABLED)
        root.bind("<a>", selectOption)
        root.bind("<b>", selectOption)
    elif player.scenecount == 1 and inputop == True:
        print("deleting scenes")
        if userinput == "a":
            del scenes[3]
            print(scenes)
            #addAction(taskview, task1)
        elif userinput == "b":
            del scenes[2]
        root.unbind("<a>")
        root.unbind("<b>")
        inputop = False
        player.scenecount += 1
        SetDialogueText(Text, scenes[player.scenecount])
    if player.scenecount == 2 and userinput == "b":
        decreaseHp(50)
    if player.scenecount == 4:
        openBattle()
    elif player.scenecount == 11:
        for i in range(3):
            openBattle()
        nextbtn.config(state=DISABLED)

def nextScene(Text):
    global inputop,battlefinished
##    scenecount = int(pdata[1])  #pass var in pdata to count
##    print(scenecount)
##    print(pdata[1])
##    if player.scenecount == 3:  #declaring scenes with battles
##        battlefinished = False
##    if battlefinished == False:
##        player.scenecount
    if player.scenecount < len(scenes) and inputop == False:
        player.scenecount += 1
        SetDialogueText(Text, scenes[player.scenecount])   #set text in dialogue screen
#        pdata[1] = str(scenecount) + "\n"   #update new count into pdata
    elif player.scenecount == len(scenes):
        SetDialogueText(Text, "End of game cuz KarWei is lazy to continue.")
    scenemanager(Text)
##    if player.scenecount < len(scenes):    #if have not reached end of scenes
##        SetDialogueText(Text, scenes[player.scenecount])   #set text in dialogue screen
##        player.scenecount += 1     #add count for next scene
###        pdata[1] = str(scenecount) + "\n"   #update new count into pdata
##    else:
##        SetDialogueText(Text, "End of game cuz KarWei is lazy to continue.")

def selectOption(event):
    global userinput,inputop
    userinput = event.char
    addAction(actionview, "Option " + userinput + " selected.")
    inputop = True
    nextbtn.config(state=ACTIVE)        

root.mainloop()
