#!/bin/python
from Request.py import Request

class MedicalFacility:
    def __init__(self, name, id, system):
        self.name = name
        self.id = id
        self.request = []
        self.system = system

    def sendRequest(self, bloodType, amount, facilityRequest):
        request = Request(bloodType, amount, facilityRequest)
        self.request.append(request)
        self.system.handleRequest(request)

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
