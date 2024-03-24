#/usr/bin/python
###
# Generating
#
#
###

def CheckIfInteger(variable):
    try:
        int(variable)
        return True
    except:
        return False
def read_weapons(filename):
    from Weapon_generator.classes import Weapon
    listOfWeapons =[]
    with open(filename) as file:
        testlistOfWeapons = file.readlines()
    for i in testlistOfWeapons:
        i = i.strip('\n')
        i = i.split(',')
        weapon = Weapon(
            weaponType = i[0],
            weaponSubtype = i[1],
            weaponName = i[2],
            weaponCost = i[3],
            weaponDmgS = i[4],
            weaponDmgM = i[5],
            weaponCrit = i[6],
            weaponRange = i[7],
            weaponWeight = i[8],
            weaponDmgType = i[9],
            weaponSpecial= i[10],
            weaponSource = i[11]
        )
        listOfWeapons.append(weapon)
    return listOfWeapons

def GenerateWeapon(weaponList, constrains):
    import numpy
    from Weapon_generator.classes import Weapon
    '''
    Randomly returns a weapon from the provided weapon list
    :param weaponlist: List which consists of multiple weapons
    :return: Randomly picked weapon from the provided list
    '''
    generatedWeapon = weaponList[numpy.random.randint(low=0, high=len(weaponList))].allVariablesAsDictionary()
    tempWeapon = Weapon(
        weaponType=generatedWeapon['weaponType'],
        weaponSubtype=generatedWeapon['weaponSubtype'],
        weaponName=generatedWeapon['weaponName'],
        weaponCost=generatedWeapon['weaponCost'],
        weaponDmgS=generatedWeapon['weaponDmgS'],
        weaponDmgM=generatedWeapon['weaponDmgM'],
        weaponCrit=generatedWeapon['weaponCrit'],
        weaponRange=generatedWeapon['weaponRange'],
        weaponWeight=generatedWeapon['weaponWeight'],
        weaponDmgType=generatedWeapon['weaponDmgType'],
        weaponSpecial=generatedWeapon['weaponSpecial'],
        weaponSource=generatedWeapon['weaponSource']
    )
    if len(CheckifConstrainsApply(tempWeapon, constrains)) > 0:
        return tempWeapon(weaponList,constrains)
    return tempWeapon
def CheckifConstrainsApply(weapon, constrains):
    '''
    Check if the defined constrains apply to the weapon

    :param weapon: Expects a weapon object
    :param constrains: Expects a dictionary
    :return: List containing the errors
    '''
    listOfErrors = []
    if len(constrains) == 0:
        return 0
    if constrains['Cost'] > weapon.CostInCopper():
        listOfErrors.append('Not enough money')
    if constrains['Type'] == weapon.weaponType:
        listOfErrors.append('weaponType constrain hit')
    if constrains['Subtype'] == weapon.weaponSubtype:
        listOfErrors.append('weaponSubType constrain hit')
    if constrains['Name'] == weapon.weaponName:
        listOfErrors.append('weaponName constrain hit')
    if constrains['DmgS'] == weapon.weaponDmgS:
        listOfErrors.append('weaponDmgS constrain hit')
    if constrains['DmgM'] == weapon.weaponDmgM:
        listOfErrors.append('weaponDmgM constrain hit')
    if constrains['Crit'] == weapon.weaponCrit:
        listOfErrors.append('weaponCrit constrain hit')
    if constrains['Range'] == weapon.weaponRange:
        listOfErrors.append('weaponRange constrain hit')
    if constrains['Weight'] == weapon.weaponWeight:
        listOfErrors.append('weaponWeight constrain hit')
    if constrains['DmgType'] == weapon.weaponDmgType:
        listOfErrors.append('weaponDmgType constrain hit')
    if constrains['Special'] == weapon.weaponSpecial:
        listOfErrors.append('weaponSpecial constrain hit')
    if constrains['Source'] == weapon.weaponSpecial:
        listOfErrors.append('Source constrain hit')
    return listOfErrors

# Constrains are build-in but currently not applied
constraints = {
    'Type': '',
    'Subtype': '',
    'Name': '',
    'Cost': '',
    'DmgS': '',
    'DmgM': '',
    'Crit': '',
    'Range': '',
    'Weight': '',
    'DmgType': '',
    'Special': '',
    'Source': ''
}
if __name__ == "__main__":
    # Setting variables required for the while loop to prevent endless
    SetPriceInCopper = 4000
    BuyPrice = 0
    BuyObjectsList = []
    rounds = 0
    totalItemCount = 0
    ListOfWeaponObjects = read_weapons('weapons.json')
    while BuyPrice <= SetPriceInCopper:
        rounds +=1
        if BuyPrice == SetPriceInCopper:
            exit()
        tempWeapon = GenerateWeapon(ListOfWeaponObjects, constraints)
        if CheckIfInteger(tempWeapon.CostInCopper()) is not True:
            continue
        elif BuyPrice <= (SetPriceInCopper-5):
            BuyPrice += int(tempWeapon.CostInCopper())
            BuyObjectsList.append(tempWeapon)
            totalItemCount +=1


    print('Generation cost {} rounds and came up with {} items:'.format(rounds,totalItemCount))
    print('MaxTreasureHoard: {}cp'.format(SetPriceInCopper))
    SortNameDict = {}
    for i in BuyObjectsList:
        if str(i.weaponName) not in SortNameDict:
            SortNameDict[str(i.weaponName)] = {
                'weaponName': str(i.weaponName),
                'weaponCount': int(0),
                'weaponList': []
            }
        SortNameDict[str(i.weaponName)]['weaponList'].append(i)
        SortNameDict[i.weaponName]['weaponCount'] += 1
    for key in SortNameDict:
        print("{}x {}".format(SortNameDict[key]['weaponCount'], key))
