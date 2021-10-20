from PIL import Image, ImageFont, ImageDraw
cardTemplate = Image.open("ressources/GeneralTemplate.png") # This is the general PNG template used for cards
titleFont = ImageFont.truetype('ressources/enchantedLand.otf', 60)
Font = ImageFont.truetype('ressources/Roboto-Regular.ttf', 30)

forceColor = ('#EA2727')
agilityColor = ('#E7E743')
intelligenceColor = ('#43C3E7')
passiveColor = ('#DFDEDF')
outline = ('#A9A9A9')

spellName = "THIS IS A TEST CARD"
spellType = "PASSIF"
editableCard = ImageDraw.Draw(cardTemplate)
editableCard.text((375,80), spellName, passiveColor, font = titleFont, anchor = 'ms', stroke_width = 3, stroke_fill = outline) # Title of the card, big text on top
editableCard.text((375,700), spellType, forceColor, font = Font, anchor = 'ms', stroke_width = 2, stroke_fill = outline) # Type of the card, below artwork

cardTemplate.save('Cards/'+spellType+'_'+spellName+'.png') # Save file in Card folder
