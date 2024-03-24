import numpy

RandomMagicItemGeneration = numpy.random.randint(low=0, high=100)
# print(RandomMagicItemGeneration)


def minorMagicItemGeneration(randomNumber):
    '''
        1-4 armor and shields
        5-9 - weapons
        10-44 potions or oils
        45-46 rings
        47-81 scrolls
        82-91 - wands
        91-100 wondrous items
    '''

    if RandomMagicItemGeneration in range(1, 4):
        print('Minor armor or Shield')
    elif RandomMagicItemGeneration in range(5, 9):
        print('Minor weapon')
    elif RandomMagicItemGeneration in range(10, 44):
        print('Minor Potions or Oils')
    elif RandomMagicItemGeneration in range(45, 46):
        print('Minor Rings')
    elif RandomMagicItemGeneration in range(47, 81):
        print('Minor Scrolls')
    elif RandomMagicItemGeneration in range(82, 91):
        print('Minor Wand')
    elif RandomMagicItemGeneration in range(91, 100):
        print('Minor Wondrous Item')

    else:
        print(True, RandomMagicItemGeneration)


def HighestWeaponBonusBasedOnAvailableFunds(availableFunds):
    RandomMagicItemGeneration = numpy.random.randint(low=0, high=100)
    Bonus = 0
    if availableFunds < 2000:
        return Bonus
    elif availableFunds >= 200000:
        Bonus = 10
    elif availableFunds > 162000:
        Bonus = 9
    elif availableFunds > 128000:
        Bonus = 8
    elif availableFunds > 98000:
        Bonus = 7
    elif availableFunds > 72000:
        Bonus = 6
    elif availableFunds > 50000:
        Bonus = 5
    elif availableFunds > 32000:
        Bonus = 4
    elif availableFunds > 18000:
        Bonus = 3
    elif availableFunds > 8000:
        Bonus = 2
    elif availableFunds > 2000:
        Bonus = 1
    return Bonus

def minorWeaponAbilityGenerator(meleeOrRanged):
    randomMinorWeaponAbilityGeneration = numpy.random.randint(low=0, high=100)
    print('random MinorWeaponAbility nr: ', randomMinorWeaponAbilityGeneration)
    bonus = 1
    try:
        if meleeOrRanged == 'Melee':
            if 1 >= randomMinorWeaponAbilityGeneration <= 10:
                name = 'Bane'
            elif 11 >= randomMinorWeaponAbilityGeneration <= 17:
                name = 'Defending'
            elif 18 >= randomMinorWeaponAbilityGeneration <= 27:
                name = 'Flaming'
            elif 28 >= randomMinorWeaponAbilityGeneration <= 37:
                name = 'Frost'
            elif 38 >= randomMinorWeaponAbilityGeneration <= 47:
                name = 'Shock'
            elif 48 >= randomMinorWeaponAbilityGeneration <= 56:
                name = 'Ghost Touch'
            elif 57 >= randomMinorWeaponAbilityGeneration <= 67:
                name = 'Keen'
            elif 68 >= randomMinorWeaponAbilityGeneration <= 71:
                name = 'Ki Focus'
            elif 72 >= randomMinorWeaponAbilityGeneration <= 75:
                name = 'Merciful'
            elif 76 >= randomMinorWeaponAbilityGeneration <= 82:
                name = 'Mighty Cleaving'
            elif 83 >= randomMinorWeaponAbilityGeneration <= 87:
                name = 'Spell Storing'
            elif 88 >= randomMinorWeaponAbilityGeneration <= 91:
                name = 'Throwing'
            elif 92 >= randomMinorWeaponAbilityGeneration <= 95:
                name = 'Thundering'
            elif 96 >= randomMinorWeaponAbilityGeneration <= 99:
                name = 'Vicious'
            else:
                minorWeaponAbilityGenerator(meleeOrRanged)
            return name, bonus
        elif meleeOrRanged == 'Ranged':
            if 1 >= randomMinorWeaponAbilityGeneration <= 12:
                name = 'Bane'
            elif 13 >= randomMinorWeaponAbilityGeneration <= 25:
                name = 'Distance'
            elif 26 >= randomMinorWeaponAbilityGeneration <= 40:
                name = 'Flaming'
            elif 41 >= randomMinorWeaponAbilityGeneration <= 55:
                name = 'Frost'
            elif 56 >= randomMinorWeaponAbilityGeneration <= 60:
                name = 'Merciful'
            elif 61 >= randomMinorWeaponAbilityGeneration <= 68:
                name = 'Returning'
            elif 69 >= randomMinorWeaponAbilityGeneration <= 83:
                name = 'Shock'
            elif 84 >= randomMinorWeaponAbilityGeneration <= 93:
                name = 'Seeking'
            elif 94 >= randomMinorWeaponAbilityGeneration <= 99:
                name = 'Thundering'
            else:
                return minorWeaponAbilityGenerator(meleeOrRanged)
            return name, bonus
        else:
            print('Not melee or Ranged')
            return minorWeaponAbilityGenerator(meleeOrRanged)
    except:
        print('Exception occured')
        return minorWeaponAbilityGenerator(meleeOrRanged)


def readJsonFileToDictionary(filename):
    '''
    Small function to read json and return a dictionary
    :param filename: relative path to file from working directory + filename
    :return:
    '''
    import json
    with open(filename) as file:
        magicItemAbilitiesDict = json.load(file)
    # print(magicItemAbilitiesDict)
    return magicItemAbilitiesDict

if __name__ == "__main__":
    AbilityDictionary = readJsonFileToDictionary('weaponEnhancements.json')
    MeleeOrRanged = numpy.random.randint(low=1, high=100)
    if int(MeleeOrRanged / 2):
        MeleeOrRanged = 'Melee'
    else:
        MeleeOrRanged = 'Ranged'

    minorWeaponAbilitydictionary = AbilityDictionary[MeleeOrRanged]['Minor']
    Ability = minorWeaponAbilityGenerator(MeleeOrRanged)
    Bonus = minorWeaponAbilitydictionary[Ability]['Bonus']
    print('type:', MeleeOrRanged)
    print('Ability:', Ability)
    print('Bonus:', Bonus)

