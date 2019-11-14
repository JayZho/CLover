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

    def getQuantity(self):
        return self._quantity

    def getBloodBags(self):
        return self._bloodBags


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
        removedBags = []
        for bloodBag in self._bloodBags:
            if(bloodBag.isExpired() == True):
                removedBags.append(bloodBag)
                self.removeBloodBag(bloodBag)
        return removedBags


    def checkCritical(self):
        return (self._quantity < self._critical)
    
    #using selection sort
    def getSortedBags(self, start, end):
        toSort = []
        for bag in self._bloodBags: #grab bags in date range
            if(start <= bag.getExpiryDate() <= end):
                toSort.append(bag)

        count = len(toSort)
        newList = []
        earliest = end
        while(count > 0):
            for each in toSort:
                if (each.getExpiryDate() <= earliest):
                    selected = each
                    earliest = each.getExpiryDate()
            newList.append(selected)
            count -= 1

        return newList           

    # Creates new blood bag, adds to list
    def addIncomingBloodBag(self, bloodId, donor, expire, arrival, origin):
        bag = BloodBag(bloodId, self._bloodType, donor, expire, arrival, origin)
        self.addBloodBag(bag)
        return bag

