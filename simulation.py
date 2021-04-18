import random
places = []
blobs = []




class Blob:
    def __init__ (self, age, productivity, location= [0,0]):
        self.age = age
        self.productivity = productivity
        self.location = location
        self.nourishment = 5
        self.isReproducing = 0
    def checkreproducing(self):
        if self.nourishment >= 8:
            self.isReproducing = 1
    def feed(self):
        for place in places:
            if place.location == self.location:
                if place.food > 0 and self.nourishment<10:
                    place.food -= 1
                    self.nourishment = 10
        

class Place:
    def __init__ (self, food, location):    
        self.location = location
        self.food = food

def initialize(foodmax, blobs, totalplaces):
    for x in range(totalplaces[0]):
        for y in range(totalplaces[1]):
            places.append(Place(random.randint(0, int(foodmax)), (int(x), int(y))))
            y+=1
        x+=1
    