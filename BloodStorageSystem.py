import datetime
from datetime import date
from MedicalFacility import MedicalFacility
from Inventory import Inventory
from flask import Flask, redirect, render_template, request, url_for, session, abort

class BloodStorageSystem:


    def __init__(self, inventory):
        self._medFacilities = [ MedicalFacility("MF1", 1, self),
                                MedicalFacility("MF2", 2, self),
                                MedicalFacility("MF3", 3, self),
                                MedicalFacility("MF4", 4, self),
                                MedicalFacility("MF5", 5, self)]
        self._inventory = inventory

        self._requestLimit = 100

        self._storageA = 0
        self._storageB = 0
        self._storageO = 0
        self._lowestLevelA = 0
        self._lowestLevelB = 0
        self._lowestLevelO = 0

        # self._bloodTypes[]



    def handleRequest(self, request):
        print("I'm here")
        bloodType = request.getType()
        amount = request.getAmount()

        #checking if they are requesting too much blood
        print(amount)
        print(self._requestLimit)
        if amount > self._requestLimit:
            print("I'm requesting too much")
            result = "error"
            return result

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





    def requestTooMuch(self):
        return render_template('failure.html')


    def addBloodType(self, bloodType):
        self._bloodTypes.append(bloodType)

    def getMFs(self):
        return self._medFacilities

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
    def addIncomingBlood(self, bloodType, donor, expire, arrival, origin):
        # TODO Parse input to check for correctness

        # Adds blood to system
        self._inventory.addIncomingBloodBag(bloodType, donor, expire, arrival, origin)
