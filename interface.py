from os import name, wait
import tkinter
from tkinter import *
from tkinter import Text,ttk , filedialog
from PIL import Image, ImageFont, ImageDraw, ImageOps,ImageTk
import textwrap

window = Tk() #create a window

# add widgets here

#================================== UI Elements ===========================================================

inputSpell = Entry(window, text="", bd=5)
inputSpell.place(x=400, y=50)

inputDesc = Text(window , width=30 , height=8)
inputDesc.place(x=400, y=150 )

dropDamage = ttk.Combobox(window,
                            values=[
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6"])
print(dict(dropDamage))
dropDamage.grid(column=0, row=1)
dropDamage.place(x=400 ,y=350)
dropDamage.current(0)

dropDice = ttk.Combobox(window,
                            values=[
                                    "d4",
                                    "d6",
                                    "d8",
                                    "d10",
                                    "d12"])
print(dict(dropDice))
dropDice.grid(column=0, row=1)
dropDice.place(x=400 ,y=400)
dropDice.current(0)

inputBonusDamage = Entry(window, text="", bd=5)
inputBonusDamage.place(x=400, y=450)

inputMana = Entry(window, text="", bd=5)
inputMana.place(x=400, y=500)

dropType = ttk.Combobox(window,
                            values=[
                                    "Force",
                                    "Agilité",
                                    "Intelligence",
                                    "Passif"])
print(dict(dropType))
dropType.grid(column=0, row=1)
dropType.place(x=400 ,y=100)
dropType.current(0)

#================================== UI Elements ===========================================================

#================================================================================================================

#cardTemplate = Image.open("ressources/GeneralTemplate.png").convert("RGBA") # This is the general PNG template used for cards
titleFont = ImageFont.truetype('ressources/enchantedLand.otf', 60)
typeFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 30)
descFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 26)
statFont = ImageFont.truetype('ressources/enchantedLand.otf', 80)

# fonts color variables
forceColor = ('#EA2727')
agilityColor = ('#E7E743')
intelligenceColor = ('#43C3E7')
passiveColor = ('#DFDEDF')
outline = ('#333333')

nameCard:filedialog

#editableCard = ImageDraw.Draw(cardTemplate)

#maxWidth = 750
#bckgImage = ""#Image.open("ressources/sap.jpg").convert("RGBA") # background image
#wPercent = (maxWidth/float(bckgImage.size[0])) # calculate ratio width between the max width and the width of the image
#newSize = int((float(bckgImage.size[1])*float(wPercent))) #Store the calculated height ratio
#bckgImage = bckgImage.resize((maxWidth,newSize), Image.ANTIALIAS) #apply new ratio to var

def add_margin(bckgImage, top, right, bottom, left, color): # creating add_margin function for later use
    width, height = bckgImage.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(bckgImage.mode, (new_width, new_height), color)
    result.paste(bckgImage, (left, top))
    return result

#bckgImage = add_margin(bckgImage, 0, 0, (1050-newSize), 0, (120, 120, 120)) # add a botoom margin calculated to fit template

# Using a wrapper for desc as it is usually long texts.

def initTemplate():
    cardTemplate  = Image.open("ressources/GeneralTemplate.png").convert("RGBA") # This is the general PNG template used for cards
    return cardTemplate

def modifCard(cardTemplate):
    editableCard = ImageDraw.Draw(cardTemplate)
    return editableCard

def getSpellName():
    return inputSpell.get()

def getSpellType():
    return dropType.get()

def getDesc(editCard):
    spellDesc = inputDesc.get("1.0","end-1c")
    wrapper = textwrap.TextWrapper(width = 60)
    wordList = wrapper.wrap(text = spellDesc)
    spellDescWrapped = ''
    for ii in wordList[:-1]:
        spellDescWrapped = spellDescWrapped + ii + '\n'
    spellDescWrapped += wordList[-1]
    editCard.text((40,750), spellDescWrapped, '#333232', font = descFont, anchor = 'ls')
    return spellDesc

def getDamage(editCard):
    if(inputBonusDamage.get() != ""):
        editCard.text((100, 1000), dropDamage.get()+dropDice.get()+"+"+inputBonusDamage.get(), forceColor, font = statFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top
    else:
       editCard.text((100, 1000), dropDamage.get()+dropDice.get(), forceColor, font = statFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top

def getMana(editCard):
    editCard.text((685, 1000), inputMana.get(), intelligenceColor, font = statFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline)

def editCard(nameSpell, typeSpell , editCard):

    match typeSpell:
        case "Force":
            editCard.text((375,80), nameSpell, forceColor, font = titleFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top
            editCard.text((375,700), typeSpell, forceColor, font = typeFont, anchor = 'ms', stroke_width = 2, stroke_fill = outline) # Type of the card, below artwork
        case "Agilité":
            editCard.text((375,80), nameSpell, agilityColor, font = titleFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top
            editCard.text((375,700), typeSpell, agilityColor, font = typeFont, anchor = 'ms', stroke_width = 2, stroke_fill = outline) # Type of the card, below artwork
        case "Intelligence":
            editCard.text((375,80), nameSpell, intelligenceColor, font = titleFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top
            editCard.text((375,700), typeSpell, intelligenceColor, font = typeFont, anchor = 'ms', stroke_width = 2, stroke_fill = outline) # Type of the card, below artwork
        case "Passif":
            editCard.text((375,80), nameSpell, passiveColor, font = titleFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top
            editCard.text((375,700), typeSpell, passiveColor, font = typeFont, anchor = 'ms', stroke_width = 2, stroke_fill = outline) # Type of the card, below artwork

#=================================================================================================================
def loadBack():
    global nameCard
    nameCard = filedialog.askopenfilename()
    return nameCard

def changeBck(name):
    maxWidth = 750
    print("Name card : " + name)
    bckgImage = Image.open(name).convert("RGBA")
    wPercent = (maxWidth/float(bckgImage.size[0]))
    newSize = int((float(bckgImage.size[1])*float(wPercent)))
    bckgImage = bckgImage.resize((maxWidth,newSize), Image.ANTIALIAS)
    bckgImage = add_margin(bckgImage, 0, 0, (1050-newSize), 0, (120, 120, 120))

    return bckgImage

def save():

    bckgImage = changeBck(nameCard)

    cardTemplate = initTemplate()
    editableCard = modifCard(cardTemplate)

    spellName = getSpellName()
    spellType = getSpellType()
    getDesc(editableCard)
    getDamage(editableCard)
    getMana(editableCard)
    editCard(spellName , spellType , editableCard)
    bckgImage.paste(cardTemplate, (0, 0), cardTemplate)
    bckgImage.save('Cards/'+spellType+'_'+spellName+'.png')

    popUp = Toplevel(window)
    popUp.title("Success !")
    popUp.geometry("400x250")
    saveLabel = Label(popUp, text = "Created card succesfully !")
    saveLabel.place(x=100, y=100)

loadFile = Button(window,text="Choose file" ,command=loadBack)
loadFile.place(x=100, y=550)
btn = Button(window,text="Generer" ,command=save)
btn.place(x=500, y=550)
labelName = Label(window, text = "Card Name")
labelName.place(x=100, y=50)
labelType = Label(window, text = "Card Type")
labelType.place(x=100, y=100)
labelDesc = Label(window, text = "Card Description")
labelDesc.place(x=100, y=150)
labelDamage = Label(window, text = "Damage")
labelDamage.place(x=100, y=350)
labelDice = Label(window, text = "Dice")
labelDice.place(x=100, y=400)
labelMana = Label(window, text = "Mana")
labelMana.place(x=100, y=500)
labelBonusD = Label(window, text = "Bonus Damage")
labelBonusD.place(x=100, y=450)
#================================== UI Window ===========================================================

window.title('CardGen pre-release version 0.000000000432')
window.geometry("750x650+10+20")
window.mainloop() #mainloop displays the window

#================================== UI Window ===========================================================
