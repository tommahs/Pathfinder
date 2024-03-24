from Magic_item_generator.magicItemgenerator import HighestWeaponBonusBasedOnAvailableFunds
from Weapon_generator.weapon_generator import *
from Magic_item_generator.magicItemgenerator import *

def ifVarInList(var, list):
    if var in list:
        return True
    else:
        return False

if __name__ == "__main__":
    # Setting variables required for the while loop to prevent endless
    SetPriceInCopper = 12000
    BuyPrice = 0
    BuyObjectsList = []
    rounds = 0
    totalItemCount = 0
    ListOfWeaponObjects = read_weapons('./Weapon_generator/weapons.json')
    ListOfWeaponEnhancements = readJsonFileToDictionary('./Magic_item_generator/weaponEnhancements.json')
    while BuyPrice < SetPriceInCopper:
        rounds +=1
        availableFunds = SetPriceInCopper-BuyPrice
        print('Round: ', rounds, '\nSetPriceInCopper: ', SetPriceInCopper, '\nBuyPrice: ', BuyPrice, '\navailableFunds: ', availableFunds)
        availableEnhancementLevel = HighestWeaponBonusBasedOnAvailableFunds(availableFunds)
        tempWeapon = GenerateWeapon(ListOfWeaponObjects, constraints)
        tempWeapon.SetEnhancementBonus(availableEnhancementLevel)
        print('availableEnhancementLevel: ', availableEnhancementLevel, 'weapon: ', tempWeapon.allVariablesAsDictionary())
        enhancementList = []
        while availableEnhancementLevel >= 1:
            # print("availableEnhancementLevel: ", availableEnhancementLevel)
            print('Enhancementlist:',enhancementList)
            generateEnhancement = numpy.random.randint(low=1, high=10)
            print('generated Enhancement: ',generateEnhancement)
            Enhancement = ""
            if availableEnhancementLevel > 5:
                if 1 >= generateEnhancement <= 5:
                    enhancementBonus = 3
                    availableEnhancementLevel -= enhancementBonus
                    print("majorWeaponAbilityGenerator() - bonus 3 for now")
                elif 6 >= generateEnhancement <= 8:
                    enhancementBonus = 2
                    availableEnhancementLevel -= enhancementBonus
                    print("mediumWeaponAbilityGenerator() bonus 2 for now")
                else:
                    Enhancement, EnhancementBonus = minorWeaponAbilityGenerator(tempWeapon.MeleeOrRanged())
            elif availableEnhancementLevel > 1:
                if 1 >= generateEnhancement <= 7:
                    enhancementBonus = 2
                    availableEnhancementLevel -= enhancementBonus
                    print("mediumWeaponAbilityGenerator() bonus 2 for now")
                else:
                    Enhancement, EnhancementBonus = minorWeaponAbilityGenerator(tempWeapon.MeleeOrRanged())
                    availableEnhancementLevel -= EnhancementBonus
            else:
                Enhancement, EnhancementBonus = minorWeaponAbilityGenerator(tempWeapon.MeleeOrRanged())
                print('Enhancement + enhancement bonus: ', Enhancement, EnhancementBonus)
                availableEnhancementLevel -= EnhancementBonus
            print()
            enhancementList.append(Enhancement)
            if Enhancement != '' and len(enhancementList) > 0:
                if Enhancement not in tempWeapon.getEnhancementList():
                    tempWeapon.AppendEnhancementToList(Enhancement)
                    print('Enhancement: ', Enhancement,'\nGetEnhancementListFromClass: ', tempWeapon.getEnhancementList())
                    print("Enhancement minorWeaponAbilityGenerator()- Minor- bonus -1 for now")
                    availableEnhancementLevel -= EnhancementBonus
                    tempWeapon.updateWeaponCost()
                    tempWeapon.updateWeaponName()
                else:
                    print('hit')
        # print(tempWeapon.allVariablesAsDictionary())
        # BuyObjectsList.append(tempWeapon)
        # print(tempWeapon.allVariablesAsDictionary())
        if CheckIfInteger(tempWeapon.CostInCopper()) is True:
            if BuyPrice <= (SetPriceInCopper-5):
                BuyPrice += int(tempWeapon.CostInCopper())
                BuyObjectsList.append(tempWeapon)
                totalItemCount +=1
        tempWeapon = ''
    print('\nResults:\n')
    print('Generation cost {} rounds and came up with {} items:'.format(rounds,totalItemCount))
    print('MaxTreasureHoard: {}cp'.format(BuyPrice))
    SortNameDict = {}
    for weapon in BuyObjectsList:
        if str(weapon.weaponName) not in SortNameDict:
            SortNameDict[str(weapon.weaponName)] = {
                'weaponName': str(weapon.weaponName),
                'weaponCount': int(0),
                'weaponList': []
            }
        SortNameDict[str(weapon.weaponName)]['weaponList'].append(weapon)
        SortNameDict[weapon.weaponName]['weaponCount'] += 1
    for key in SortNameDict:
        print("{}x {}".format(SortNameDict[key]['weaponCount'], key))
        counter = SortNameDict[key]['weaponCount']
        # for weapon in SortNameDict[key]['weaponList']:
        #     counter +=1
        #     # if len(weapon.weaponEnhancementsList) > 0:
        #     #     print(weapon.getEnhancementList(), print(weapon.weaponCost), print(weapon.allVariablesAsDictionary()))