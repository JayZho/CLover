import datetime
from datetime import date
from MedicalFacility import MedicalFacility

class BloodStorageSystem:


    def __init__(self):
        self._medFacilities = []
        self._requestLimit = 100

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
        type = request.getType()
        amount = request.getAmount()

        #checking if they are requesting too much blood

        if type == 'A':
            bloodType = self._bloodTypes[0]

        elif type == 'B':
            bloodType = self._bloodTypes[1]

        elif type == 'AB':
            bloodType = self._bloodTypes[2]

        elif type == 'O':
            bloodType = self._bloodTypes[3]


        if amount < 0 or amount > self._requestLimit :
            print("request rejected")
            result = "error"
            return result

        if (bloodType.getQuantity() - amount) < bloodType.getCritical():
            amount = bloodType.getQuantity() - bloodType.getCritical()

        #read csv file or use a list of blood
        bloodBags = bloodType.getBloodBags()
        #sort the blood bags based on expiry dates
        #implement the sort algorithm instead of using the sort function
        sortedBloodBags = self.bubbleSort(bloodBags)
        #suppose we want to remove 10 bags
        toSendList = sortedBloodBags[:amount]
        #update our database
        bloodType.setBloodBags(sortedBloodBags[amount:])
       

    def getAllBags(self, whichType):
        for eachType in self._bloodTypes:
            if eachType.getBloodType() == whichType:
                return eachType.getBloodBags()

    def getSortedBags(self, start, end, whichType):
        for eachType in self._bloodTypes:
            if eachType.getBloodType() == whichType:
                return eachType.getSortedBags(start, end)


    def getQuantity(self, whichType):
        for eachType in self._bloodTypes:
            if eachType.getBloodType() == whichType:
                return eachType.getQuantity()


    def bubbleSort(self, bloodBags):
        i = len(bloodBags) - 1
        while (i > 0):
            j = 0
            while ( j < i):
                if (bloodBags[j].getExpiryDate() > bloodBags[j+1].getExpiryDate()):
                    temporary = bloodBags[j]
                    bloodBags[j] = bloodBags[j+1]
                    bloodBags[j+1] = temporary
                j += 1
            i -= 1

        return bloodBags

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
    def checkExpiredBlood(self):
        for bloodType in self._bloodTypes:
            bloodType.removeExpiredBlood()


    def checkCritical(self):
        for bloodType in self._bloodTypes:
            if(bloodType.checkCritical):
                self.giveWarning(bloodType.getType())

    # Add incoming blood bag to inventory
    def addIncomingBlood(self, bloodId, bloodType, donor, expire, arrival, origin):
        # TODO Parse input to check for correctness
        bloodBag = None

        # Adds blood to system
        for bType in self._bloodTypes:
            # Equals correct blood type, add blood
            if bloodType == bType.getBloodType():
                bloodBag = bType.addIncomingBloodBag(bloodId, donor, expire, arrival, origin)
                break
        return bloodBag