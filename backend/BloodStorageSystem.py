import datetime
from datetime import date
from MedicalFacility.py import MedicalFacility

class BloodStorageSystem:


    def __init__(self, inventory):
        self._medFacilities = [ MedicalFacility(A, 1, self)]
        self._inventory = inventory
        self._lowestLevelA = 0
        self._lowestLevelB = 0
        self._lowestLevelO = 0
        self._requestLimit = 0
        self._storageA = 0
        self._storageB = 0
        self._storageO = 0


    def handleRequest(self, request):
        type = request.getType()
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

    def giveWarning(self):
        pass
