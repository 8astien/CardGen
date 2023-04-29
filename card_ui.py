import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageFont, ImageDraw, ImageOps
import textwrap

from card import Card

class CardUI:
    def __init__(self, master):
        # Parent tkinter window
        self.master = master

        # fonts declarations
        self.titleFont = ImageFont.truetype('ressources/enchantedLand.otf', 60)
        self.typeFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 30)
        self.descFont = ImageFont.truetype('ressources/Roboto-Regular.ttf', 26)
        self.statFont = ImageFont.truetype('ressources/enchantedLand.otf', 80)

        # fonts color declarations
        self.forceColor = '#EA2727'
        self.agilityColor = '#E7E743'
        self.intelligenceColor = '#43C3E7'
        self.passiveColor = '#DFDEDF'
        self.outline = '#333333'

        self.create_ui_elements()

    def create_ui_elements(self):
        tk.Label(self.master, text="Spell Name").place(x=100, y=50)
        self.inputSpell = tk.Entry(self.master, bd=5)
        self.inputSpell.place(x=400, y=50)

        tk.Label(self.master, text="Description").place(x=100, y=150)
        self.inputDesc = tk.Text(self.master, width=30, height=8)
        self.inputDesc.place(x=400, y=150)

        tk.Label(self.master, text="Damage").place(x=100, y=350)
        self.dropDamage = ttk.Combobox(self.master, values=["1", "2", "3", "4", "5", "6"])
        self.dropDamage.place(x=400, y=350)
        self.dropDamage.current(0)

        tk.Label(self.master, text="Dice").place(x=100, y=400)
        self.dropDice = ttk.Combobox(self.master, values=["d4", "d6", "d8", "d10", "d12"])
        self.dropDice.place(x=400, y=400)
        self.dropDice.current(0)

        tk.Label(self.master, text="Bonus Damage").place(x=100, y=450)
        self.inputBonusDamage = tk.Entry(self.master, bd=5)
        self.inputBonusDamage.place(x=400, y=450)

        tk.Label(self.master, text="Mana").place(x=100, y=500)
        self.inputMana = tk.Entry(self.master, bd=5)
        self.inputMana.place(x=400, y=500)

        tk.Label(self.master, text="Type").place(x=100, y=100)
        self.dropType = ttk.Combobox(self.master, values=["Force", "Agilité", "Intelligence", "Passif"])
        self.dropType.place(x=400, y=100)
        self.dropType.current(0)

        self.loadFile = tk.Button(self.master, text="Choose file", command=self.load_back)
        self.loadFile.place(x=100, y=550)

        self.saveBtn = tk.Button(self.master, text="Generer", command=self.save, state=tk.DISABLED)
        self.saveBtn.place(x=500, y=550)

    def load_back(self):
        self.nameCard = filedialog.askopenfilename()
        if self.nameCard:
            self.saveBtn.config(state=tk.NORMAL)
        return self.nameCard

    def add_margin(self, bckgImage, top, right, bottom, left, color):
        width, height = bckgImage.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(bckgImage.mode, (new_width, new_height), color)
        result.paste(bckgImage, (left, top))
        return result

    def changeBck(self, name):
        maxWidth = 750
        bckgImage = Image.open(name).convert("RGBA")
        wPercent = (maxWidth / float(bckgImage.size[0]))
        newSize = int((float(bckgImage.size[1]) * float(wPercent)))
        bckgImage = bckgImage.resize((maxWidth, newSize), Image.ANTIALIAS)
        bckgImage = self.add_margin(bckgImage, 0, 0, (1050 - newSize), 0, (120, 120, 120))
        return bckgImage

    def initTemplate(self):
        cardTemplate = Image.open("ressources/GeneralTemplate.png").convert("RGBA")
        return cardTemplate

    def modifCard(self, cardTemplate):
        editableCard = ImageDraw.Draw(cardTemplate)
        return editableCard

    def getSpellName(self):
        return self.inputSpell.get()

    def getSpellType(self):
        return self.dropType.get()
    
    def getDesc(self, editCard):
        spellDesc = self.inputDesc.get("1.0", "end-1c")
        wrapper = textwrap.TextWrapper(width=60)
        wordList = wrapper.wrap(text=spellDesc)
        spellDescWrapped = ''
        for ii in wordList[:-1]:
            spellDescWrapped = spellDescWrapped + ii + '\n'
        spellDescWrapped += wordList[-1]
        editCard.text((40, 750), spellDescWrapped, '#333232', font=self.descFont, anchor='ls')
        return spellDesc

    def getDamage(self, editCard):
        if self.inputBonusDamage.get() != "":
            editCard.text((100, 1000), self.dropDamage.get() + self.dropDice.get() + "+" + self.inputBonusDamage.get(), self.forceColor,
                        font=self.statFont, anchor='ms', stroke_width=3, stroke_fill=self.outline)
        else:
            editCard.text((100, 1000), self.dropDamage.get() + self.dropDice.get(), self.forceColor, font=self.statFont, anchor='ms',
                        stroke_width=3, stroke_fill=self.outline)

    def getMana(self, editCard):
        editCard.text((685, 1000), self.inputMana.get(), self.intelligenceColor, font=self.statFont, anchor='ms', stroke_width=3,
                    stroke_fill=self.outline)

    def editCard(self, nameSpell, typeSpell, editCard):
        match typeSpell:
            case "Force":
                editCard.text((375, 80), nameSpell, self.forceColor, font=self.titleFont, anchor='ms', stroke_width=3,
                            stroke_fill=self.outline)
                editCard.text((375, 700), typeSpell, self.forceColor, font=self.typeFont, anchor='ms', stroke_width=2,
                            stroke_fill=self.outline)
            case "Agilité":
                editCard.text((375, 80), nameSpell, self.agilityColor, font=self.titleFont, anchor='ms', stroke_width=3,
                            stroke_fill=self.outline)
                editCard.text((375, 700), typeSpell, self.agilityColor, font=self.typeFont, anchor='ms', stroke_width=2,
                            stroke_fill=self.outline)
            case "Intelligence":
                editCard.text((375, 80), nameSpell, self.intelligenceColor, font=self.titleFont, anchor='ms', stroke_width=3,
                            stroke_fill=self.outline)
                editCard.text((375, 700), typeSpell, self.intelligenceColor, font=self.typeFont, anchor='ms', stroke_width=2,
                            stroke_fill=self.outline)
            case "Passif":
                editCard.text((375, 80), nameSpell, self.passiveColor, font=self.titleFont, anchor='ms', stroke_width=3,
                            stroke_fill=self.outline)
                editCard.text((375, 700), typeSpell, self.passiveColor, font=self.typeFont, anchor='ms', stroke_width=2,
                            stroke_fill=self.outline)

    def save(self):
        bckgImage = self.changeBck(self.nameCard)

        cardTemplate = self.initTemplate()
        editableCard = self.modifCard(cardTemplate)

        spellName = self.getSpellName()
        spellType = self.getSpellType()
        spellDesc = self.getDesc(editableCard)

        self.getDamage(editableCard)
        self.getMana(editableCard)
        self.editCard(spellName, spellType, editableCard)
        bckgImage.paste(cardTemplate, (0, 0), cardTemplate)
        bckgImage.save('Cards/' + spellType + '_' + spellName + '.png')

        card = Card(spellName, spellType, spellDesc, self.dropDamage.get(), self.dropDice.get(),
            self.inputBonusDamage.get(), self.inputMana.get())
        card.save_to_csv(f'database/{spellName}.csv')

        popUp = tk.Toplevel(self.master)
        popUp.title("Success !")
        popUp.geometry("400x250")
        saveLabel = tk.Label(popUp, text="Created card successfully !")
        saveLabel.place(x=100, y=100)
