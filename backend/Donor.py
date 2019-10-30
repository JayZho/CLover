#!/bin/python

class Donor:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_donor_name(self):
        return self.name

    def set_donor_name(self, name):
        self.name = name

    def get_donor_id(self):
        return self.id

    def set_donor_id(self, id):
        self.id = id