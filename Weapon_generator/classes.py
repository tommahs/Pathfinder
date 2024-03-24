class Weapon():
    def __init__(self, weaponName, weaponType, weaponSubtype, weaponCost, weaponDmgS, weaponDmgM, weaponCrit, weaponRange, weaponWeight, weaponDmgType, weaponSpecial, weaponSource):
        self.weaponName = weaponName
        self.weaponType = weaponType
        self.weaponSubtype = weaponSubtype
        self.weaponCost = weaponCost
        self.weaponDmgS = weaponDmgS
        self.weaponDmgM = weaponDmgM
        self.weaponCrit = weaponCrit
        self.weaponRange = weaponRange
        self.weaponWeight = weaponWeight
        self.weaponDmgType = weaponDmgType
        self.weaponSpecial = weaponSpecial
        self.weaponSource = weaponSource
        self.weaponEnhancementBonus = 0
        self.weaponEnhancementsList = []
    def allVariablesAsDictionary(self):
        self.variableDictionary = {
            'weaponName': self.weaponName,
            'weaponType': self.weaponType,
            'weaponSubtype': self.weaponSubtype,
            'weaponCost': self.weaponCost,
            'weaponDmgS': self.weaponDmgS,
            'weaponDmgM': self.weaponDmgM,
            'weaponCrit': self.weaponCrit,
            'weaponRange': self.weaponRange,
            'weaponWeight': self.weaponWeight,
            'weaponDmgType': self.weaponDmgType,
            'weaponSpecial': self.weaponSpecial,
            'weaponSource': self.weaponSource,
            'weaponEnhancementBonus': self.weaponEnhancementBonus,
            'weaponEnhancementsList': self.weaponEnhancementsList
        }
        return self.variableDictionary
    def updateWeaponCost(self):
        if self.weaponEnhancementBonus > 0:
            try:
                oldcost = int(self.CostInCopper())
                newcost = self.weaponEnhancementBonus * self.weaponEnhancementBonus * 2000 + oldcost
            except ValueError:
                newcost = self.weaponEnhancementBonus * self.weaponEnhancementBonus * 2000
            self.weaponCost = '{} cp'.format(newcost)
            return True
        else:
            return True

    def updateWeaponName(self):
        for enhancement in self.weaponEnhancementsList:
            print('updateWeaponName Enhancement list: ', self.weaponEnhancementsList)
            self.weaponName = '{} {}'.format(enhancement, self.weaponName)
            print('updated weaponName in class: ', self.weaponName)
        return True

    def CostInCopper(self):
        '''
        Calculate the copper value of the item based on the weaponCost variable.
        :return: integer of the copper value of the weaponCost variable
        '''
        if 'pp' in self.weaponCost:
            cost = int(self.weaponCost.split(' ')[0])*1000
            return str(cost)
        elif 'gp' in self.weaponCost:
            cost = int(self.weaponCost.split(' ')[0])*100
            return str(cost)
        elif 'sp' in self.weaponCost:
            cost = int(self.weaponCost.split(' ')[0])*10
            return str(cost)
        elif 'cp' in self.weaponCost:
            cost = int(self.weaponCost.split(' ')[0])
            return str(cost)
        else:
            return str(self.weaponCost)

    def SetEnhancementBonus(self, weaponEnhancementBonus):
        self.weaponEnhancementBonus = weaponEnhancementBonus
        # return True

    def SetEnhancementList(self, weaponEnhancementsList):
        self.weaponEnhancementsList = weaponEnhancementsList
        return True
    def getEnhancementList(self):
        return self.weaponEnhancementsList

    def AppendEnhancementToList(self,weaponEnhancement):
        self.weaponEnhancementsList.append(weaponEnhancement)
        return True

    def MeleeOrRanged(self):
        if 'Melee' in self.weaponSubtype:
            return 'Melee'
        elif 'Ranged' in self.weaponSubtype:
            return 'Ranged'
        elif 'Unarmed' in self.weaponSubtype:
            return 'Melee'
        else:
            return 'weapon.Subtype is not Melee or Ranged but: {} '.format(self.weaponSubtype)

class Armor():
    def __init__(self, armorName, armorType, armorSubtype, armorCost, armorDmgS, armorDmgM, armorCrit, armorRange, armorWeight, armorDmgType, armorSpecial, armorSource):
     self.armorName = armorName
     self.armorType = armorType
     self.armorSubtype = armorSubtype
     self.armorCost = armorCost
     self.armorDmgS = armorDmgS
     self.armorDmgM = armorDmgM
     self.armorCrit = armorCrit
     self.armorRange = armorRange
     self.armorWeight = armorWeight
     self.armorDmgType = armorDmgType
     self.armorSpecial = armorSpecial
     self.armorSource = armorSource
    def allVariablesAsDictionary(self):
        self.variableDictionary = {
            'armorName': self.armorName,
            'armorType': self.armorType,
            'armorSubtype': self.armorSubtype,
            'armorCost': self.armorCost,
            'armorDmgS': self.armorDmgS,
            'armorDmgM': self.armorDmgM,
            'armorCrit': self.armorCrit,
            'armorRange': self.armorRange,
            'armorWeight': self.armorWeight,
            'armorDmgType': self.armorDmgType,
            'armorSpecial': self.armorSpecial,
            'armorSource': self.armorSource
        }
        return self.variableDictionary

    def CostInCopper(self):
        '''
        Calculate the copper value of the item based on the armorCost variable.
        :return: integer of the copper value of the armorCost variable
        '''
        if 'gp' in self.armorCost:
            cost = int(self.armorCost.split(' ')[0])*100
            return str(cost)
        elif 'sp' in self.armorCost:
            cost = int(self.armorCost.split(' ')[0])*10
            return str(cost)
        else:
            return str(self.armorCost)


