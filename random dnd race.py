from random import randint

races = ['a Dwarf', 'an Elf', 'a Halfling', 'a Human', 'a Dragonborn', 'a Gnome', 'a Half-elf', 'a Half-orc', 'a Tiefling']
race_list_len = len(races) - 1
player_race = races[randint(0, race_list_len)].lower()

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock',
 'Wizard']
class_list_len = len(classes) - 1
player_class = classes[randint(0, class_list_len)].lower()

backgrounds = ['an Acolyte', 'a Charlatan', 'a Criminal', 'an Entertainer','a Folk Hero', 'a Guild Artisan', 'a Hermit',
 'a Noble', 'an Outlander', 'a Sage','a Sailor', 'a Soldier','an Urchin', 'a big huge dummy']
background_list_len = len(backgrounds) - 1
player_background = backgrounds[randint(0, background_list_len)].lower()

print ('I am %s %s. I was once %s.' % (player_race, player_class, player_background))