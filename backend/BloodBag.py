import datetime
from datetime import date

class BloodBag:


    def __init__(self, id, bloodType, donor, expire, arrival, origin):
        self._id = id #int 
        self._type = bloodType #A/B/AB/O
        self._donor = donor #donor instance
        self._expiryDate = expire 
        self._arrivalDate = arrival
        self._origin = origin
    
    def getType(self):
        return self._type
    
    def getDonor(self):
        return self._donor

    def getArrivalDate(self):
        return self._arrivalDate

    def getOrigin(self):
        return self._origin

    #check if the blood is expired
    def isExpired(self):
        return (self._expiryDate <= date.today())

    def getSortedBags(self, start, end):
        

    
    