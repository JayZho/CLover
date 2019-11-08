import datetime
from datetime import date

class BloodBag:


    def __init__(self, bloodType, donor, expire, arrival, origin):
        self._bloodType = bloodType
        self._donor = donor
        self._expiryDate = expire
        self._arrivalDate = arrival
        self._origin = origin
    
    def getType(self):
        return self._bloodType
    
    def getDonor(self):
        return self._donor

    def getArrivalDate(self):
        return self._arrivalDate

    def getOrigin(self):
        return self._origin

    #check if the blood is expired
    def isExpired(self):
        return (self._expiryDate <= date.today())