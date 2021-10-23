import tkinter
from tkinter import *
from tkinter import Text,ttk
from PIL import Image, ImageFont, ImageDraw, ImageOps
import textwrap

window = Tk() #create a window

# add widgets here


#================================== UI Elements ===========================================================

inputSpell = Entry(window, text="", bd=5)
inputSpell.place(x=600, y=50)

inputDesc = Text(window , width=40 , height=10)
inputDesc.place(x=600, y=150 )


dropType = ttk.Combobox(window, 
                            values=[
                                    "Force", 
                                    "Agilité",
                                    "Intelligence",
                                    "Passif"])
print(dict(dropType)) 
dropType.grid(column=0, row=1)
dropType.place(x=600 ,y=100)
dropType.current(0)
#================================== UI Elements ===========================================================

#================================================================================================================


cardTemplate = Image.open("ressources/GeneralTemplate.png").convert("RGBA") # This is the general PNG template used for cards
titleFont = ImageFont.truetype('ressources/enchantedLand.otf', 60)
typeFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 30)
descFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 26)
# fonts color variables
forceColor = ('#EA2727')
agilityColor = ('#E7E743')
intelligenceColor = ('#43C3E7')
passiveColor = ('#DFDEDF')
outline = ('#333333')

editableCard = ImageDraw.Draw(cardTemplate)

maxWidth = 750
bckgImage = Image.open("ressources/sap.jpg").convert("RGBA") # background image
wPercent = (maxWidth/float(bckgImage.size[0])) # calculate ratio width between the max width and the width of the image
newSize = int((float(bckgImage.size[1])*float(wPercent))) #Store the calculated height ratio
bckgImage = bckgImage.resize((maxWidth,newSize), Image.ANTIALIAS) #apply new ratio to var


def add_margin(bckgImage, top, right, bottom, left, color): # creating add_margin function for later use
    width, height = bckgImage.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(bckgImage.mode, (new_width, new_height), color)
    result.paste(bckgImage, (left, top))
    return result

bckgImage = add_margin(bckgImage, 0, 0, (1050-newSize), 0, (120, 120, 120)) # add a botoom margin calculated to fit template

# Using a wrapper for desc as it is usually long texts.

def getSpellName():
    spellName = inputSpell.get()
    return spellName

def getSpellType():
    spellType = dropType.get()
    return spellType

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

def editCard(nameSpell, typeSpell , editCard):
    editCard = ImageDraw.Draw(cardTemplate)

    print('TypeSpell : ' + typeSpell)

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

def save(): 
    spellName = getSpellName()
    spellType = getSpellType()
    spellDesc = getDesc(editableCard)
    editCard(spellName , spellType , editableCard)
    bckgImage.paste(cardTemplate, (0, 0), cardTemplate)
    bckgImage.save('Cards/'+spellType+'_'+spellName+'.png')
    print('Created card succesfully !')


btn = Button(window,text="Generer" ,command=save)
btn.place(x=900, y=50)
labelName = Label(window, text = "Card Name")
labelName.place(x=450, y=50)
labelType = Label(window, text = "Card Type")
labelType.place(x=450, y=100)
labelDesc = Label(window, text = "Card Description")
labelDesc.place(x=450, y=150)
#================================== UI Window ===========================================================

window.title('CardGen pre-release version 0.000000000432')
window.geometry("1024x720+10+20")
window.mainloop() #mainloop displays the window

#================================== UI Window ===========================================================
