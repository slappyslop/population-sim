import random
import numpy
places = []
blobs = []
locations = []



class Blob:
    def __init__ (self, age, productivity, location= [0,0]):
        self.age = age
        self.productivity = productivity
        self.location = location
        self.nourishment = 5
        self.isReproducing = 0
        self.oldlocation = []

    def checkreproducing(self):
        if self.nourishment >= 8:
            self.isReproducing = 1
            self.nourishment-= 5

    def feed(self):
        for place in places:
            if place.location == self.location:
                if place.food > 0 and self.nourishment<10:
                    place.food -= 1
                    self.nourishment = 10

    def move(self):
        
        self.oldlocation.append(self.location[0])
        self.oldlocation.append(self.location[1])
        self.location[0]+=  random.randint(-1, 1)
        self.location[1]+= random.randint(-1, 1)
        while self.location not in locations:
            self.location = self.oldlocation
            self.location[0]+= random.randint(-1, 1)
            self.location[1]+= random.randint(-1, 1)
    
        if self.location == self.oldlocation:
            pass
        elif numpy.subtract(self.location, self.oldlocation) in [[1,1], [1, -1],[-1, 1], [-1, -1]]:
                    self.nourishment -= 2
        else:
            self.nourishment -=1
            



class Place:
    def __init__ (self, food, location):    
        self.location = location
        self.food = food

def initialize(foodmax, totalblobs, totalplaces):
    for x in range(totalplaces[0]):
        for y in range(totalplaces[1]):
            places.append(Place(random.randint(0, int(foodmax)), (int(x), int(y))))
            y+=1
        x+=1
    for place in places:
        locations.append(place.location)
    for i in range(totalblobs):
        blobs.append(Blob(random.randint(0, 5), 0, location = [random.randint(0, totalplaces[0]-1), random.randint(0, totalplaces[1]-1)]))
        i+=1

initialize (1, 1, [2,2])
for i in range(10):
    for blob in blobs:
        print(str(blob.location[0]) + str(blob.location[1]) + "before move")
        print(str(blob.nourishment) + "nourishment before move")
        blob.move()
        print(str(blob.location[0]) + str(blob.location[1])+ "after move")
        print(blob.nourishment + "after move")
        