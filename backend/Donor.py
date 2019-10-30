#!/bin/python

class Donor:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def Request(self, bloodType, amount):
        raise NotImplementedError
    
