import textwrap
from PIL import Image, ImageFont, ImageDraw

cardTemplate = Image.open("ressources/GeneralTemplate.png") # This is the general PNG template used for cards
titleFont = ImageFont.truetype('ressources/enchantedLand.otf', 60)
typeFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 30)
descFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 26)

# fonts color variables
forceColor = ('#EA2727')
agilityColor = ('#E7E743')
intelligenceColor = ('#43C3E7')
passiveColor = ('#DFDEDF')
outline = ('#333333')

# content of the card, declared here by var but will get modified once JSON file is loaded
spellName = "THIS IS A TEST CARD"
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
editableCard.text((375,700), spellType, forceColor, font = typeFont, anchor = 'ms', stroke_width = 2, stroke_fill = outline) # Type of the card, below artwork
editableCard.text((40,750), spellDescWrapped, '#333232', font = descFont, anchor = 'ls')

cardTemplate.save('Cards/'+spellType+'_'+spellName+'.png') # Save file in Card folder
print('Created card succesfully !')
