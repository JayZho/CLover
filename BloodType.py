import datetime
from datetime import date
from BloodBag import BloodBag

class BloodType:


    def __init__(self, bloodType, lowest):
        self._bloodType = bloodType
        self._quantity = 0
        self._bloodBags = []
        self._critical = lowest

    def getBloodType(self):
        return self._bloodType

    def getBloodBags(self):
        return self._bloodBags

    def getQuantity(self):
        return self._quantity

    def getCritical(self):
        return self._critical

    def setBloodBags(self, bloodBags):
        self._bloodBags = bloodBags
        self._quantity = len(bloodBags)


    #takes in a BloodBag instance
    #remove from '_bloodBags'
    def removeBloodBag(self, bag):
        self._bloodBags.remove(bag)
        self._quantity -= 1

    #takes in a BloodBag instance
    #append to '_bloodBags'
    def addBloodBag(self, bag):
        self._bloodBags.append(bag)
        self._quantity += 1

    #removes all expired blood bags from '_bloodBags'
    def removeExpiredBlood(self):
        for bloodBag in self._bloodBags:
            if(bloodBag.isExpired() == True):
                self.removeBloodBag(bloodBag)

    def checkCritical(self):
        return (self._quantity < self._critical)


    # Creates new blood bag, adds to list
    def addIncomingBloodBag(self, bloodId, donor, expire, arrival, origin):
        bag = BloodBag(bloodId, self._bloodType, donor, expire, arrival, origin)
        self.addBloodBag(bag)
        return bag
