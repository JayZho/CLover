import datetime
from datetime import date
from MedicalFacility import MedicalFacility
from Inventory import Inventory

class BloodStorageSystem:


    def __init__(self):
        self._medFacilities = []
        self._requestLimit = 0

        self._storageA = 0
        self._storageB = 0
        self._storageO = 0
        self._lowestLevelA = 0
        self._lowestLevelB = 0
        self._lowestLevelO = 0

        self._bloodTypes = []

    def addMedFacility(self, medFacility):
        self._medFacilities.append(medFacility)

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
    
    # Add incoming blood bag to inventory
    def addIncomingBlood(self, bloodId, bloodType, donor, expire, arrival, origin):
        # TODO Parse input to check for correctness

        # Adds blood to system
        for bType in self._bloodTypes:
            # Equals correct blood type, add blood
            if bloodType == bType.getBloodTypes():
                bType.addIncomingBloodBag(donor, expire, arrival, origin)
                break
