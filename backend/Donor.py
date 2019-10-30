#!/bin/python

class Donor:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id