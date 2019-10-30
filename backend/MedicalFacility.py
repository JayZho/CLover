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

    def accept_request(self, Request):
        raise NotImplementedError
    
    def get_MF_name(self):
        return self.name

    def set_MF_name(self, name):
        self.name = name

    def get_MF_id(self):
        return self.id

    def set_MF_id(self, id):
        self.id = id

    def get_MF_request(self):
        return self.request

    def set_MF_request(self, Request):
        self.request.append(Request)
