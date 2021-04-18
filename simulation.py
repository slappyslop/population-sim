import random

class Blob:
    def __init__ (self, age, productivity, locationx= (0,0)):
        self.age = age
        self.productivity = productivity
        self.location = location
        self.nourishment = 5
        self.isReproducing = 0
    def checkreproducing(self):
        if self.nourishment >= 8:
            self.isReproducing = 1
        

    




