import datetime
from datetime import date
from BloodBag import BloodBag

class BloodType:


    def __init__(self, type, limit):
        self._type = type
        self._quantity = 0
        self._bloodBags = []
        self._limit = limit
    
    def getType(self):
        return self._type

    def getQuantity(self):
        return self._quantity


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





    
