#!/bin/python

class MedicalFacility:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.request = []
    
    def Request(self, bloodType, amount, facilityRequest):
        self.request.append(facilityRequest)
        raise NotImplementedError

    def send_blood(self, amount, listBloodBag):
        raise NotImplementedError

