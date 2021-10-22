#!/usr/bin/env python3
import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageOps

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

# content of the card, declared here by var but will get modified once called file is loaded
spellName = "TEST CARD USED FOR TESTING"
spellType = "PASSIF"
spellDesc = "This is a test card, using wrap in order for the text not to go out of the card template otherwise it swould be cringe bro."

# Using a wrapper for desc as it is usually long texts.
wrapper = textwrap.TextWrapper(width = 60)
wordList = wrapper.wrap(text = spellDesc)
spellDescWrapped = ''
for ii in wordList[:-1]:
    spellDescWrapped = spellDescWrapped + ii + '\n'
spellDescWrapped += wordList[-1]

editableCard = ImageDraw.Draw(cardTemplate)

editableCard.text((375,80), spellName, passiveColor, font = titleFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top
editableCard.text((375,700), spellType, passiveColor, font = typeFont, anchor = 'ms', stroke_width = 2, stroke_fill = outline) # Type of the card, below artwork
editableCard.text((40,750), spellDescWrapped, '#333232', font = descFont, anchor = 'ls')

bckgImage.paste(cardTemplate, (0, 0), cardTemplate)

bckgImage.save('Cards/'+spellType+'_'+spellName+'.png') # Save file in Card folder

print('Created card succesfully !')
