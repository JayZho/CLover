

class Request:

    def __init__(self, bloodType, amount, mfId, notes):
        self._type = bloodType
        self._amount = amount
        self._mfId = mfId
        self._notes = notes

    def getType(self):
        return self._type

    def getMfId(self):
        return self._mfId

    def getAmount(self):
        return self._amount

    def getNotes(self):
        return self._notes

    def setType(self, bloodType):
        self._type = bloodType

    def setAmount(self, amount):
        self._amount = amount

    def setMfId(self,mfId ):
        self._mfId = mfId


    def setNotes(self, notes):
        self._notes = notes
