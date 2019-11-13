import datetime
from datetime import date
from MedicalFacility.py import MedicalFacility
from BloodType import BloodType

class BloodStorageSystem:


    def __init__(self, inventory):
        self._medFacilities = [ MedicalFacility(A, 1, self)]
        self._inventory = inventory
        
        self._requestLimit = 0

        self._storageA = 0
        self._storageB = 0
        self._storageO = 0
        self._storageAB = 0
        self._lowestLevelA = 0
        self._lowestLevelB = 0
        self._lowestLevelO = 0
        self._lowestLevelAB = 0

        self._typeA = BloodType(self, "A", self._lowestLevelA)
        self._typeB = BloodType(self, "B", self._lowestLevelB)
        self._typeO = BloodType(self, "O", self._lowestLevelO)
        self._typeAB = BloodType(self, "AB", self._lowestLevelAB)
       


    def handleRequest(self, request):
        blodType = request.getType()
        amount = request.getAmount()

        #checking if they are requesting too much blood
        if amount > self._requestLimit:
            self.requestTooMuch()

        if type == 'A':
            amountLeft = self._storageA - amount
            if amountLeft < self._lowestLevelA:
                amount = self._storageA - self._lowestLevelA

        elif type == 'B':
            amountLeft = self._storageB - amount
            if amountLeft < self._lowestLevelB:
                amount = self._storageB - self._lowestLevelB

        elif type == 'O':
            amountLeft = self._storageO - amount
            if amountLeft < self._lowestLevelO:
                amount = self._storageO - self._lowestLevelO


        #read csv file or use a list of blood
        bloodBags = []
        #sort the blood bags based on expiry dates
        #implement the sort algorithm instead of using the sort function
        sortedBloodBags = sort(bloodBags)
        #suppose we want to remove 10 bags
        toSendList = sortedBloodBags[:amount]
        #update our database
        bloodBags = sortedBloodBags[amount:]
        




    def requestTooMuch():
        pass


    def addBloodType(self, bloodType):
        self._bloodTypes.append(bloodType)

    def getBloodTypes(self):
        return self._bloodTypes

    def getQuantity(self, bType):
        for each in _bloodTypes:
            if(each.getType == bType):
                return each.getQuantity

    def giveWarning(self, blood):
        print("Storage of type ", blood, " is below critical!")

    #check and remove expired blood bags
    def checkExpriedBlood(self):
        for bloodType in self._bloodTypes:
            bloodType.removeExpiredBlood()


    def checkCritical(self):
        for bloodType in self._bloodTypes:
            if(bloodType.checkCritical):
                self.giveWarning(bloodType.getType())

    def getListBloodType(self, BloodType, startDate, endDate):
        if (self._typeA == BloodType):
            return self._typeA.getSortedBags(startDate, endDate)
        elif self._typeB == BloodType):
            return self._typeB.getSortedBags(startDate, endDate)
        elif self._typeO == BloodType):
            return self._typeO.getSortedBags(startDate, endDate)
        elif self._typeAB == BloodType):
            return self._typeAB.getSortedBags(startDate, endDate)
        else:
            return null
        
            
            
