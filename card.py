import csv

class Card:
    def __init__(self, name, type, description, damage, dice, bonus_damage, mana):
        self.name = name
        self.type = type
        self.description = description
        self.damage = damage
        self.dice = dice
        self.bonus_damage = bonus_damage
        self.mana = mana

    def save_to_csv(self, filename):
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['name', 'type', 'description', 'damage', 'dice', 'bonus_damage', 'mana']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': self.name, 'type': self.type, 'description': self.description, 'damage': self.damage, 
                             'dice': self.dice, 'bonus_damage': self.bonus_damage, 'mana': self.mana})
    
