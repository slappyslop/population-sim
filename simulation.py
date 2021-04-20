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
        self.oldlocation = tuple(location)

    def checkreproducing(self):
        if self.nourishment >= 8:
            self.isReproducing = 1
            self.nourishment-= 5

    def feed(self):
        for place in places:
            if place.location == tuple(self.location):
                if place.food > 0 and self.nourishment<10:
                    place.food -= 1
                    self.nourishment = 10
                    return
                else: 
                    return 
    def move(self):
        self.location[0]+=  random.randint(-1, 1)
        self.location[1]+= random.randint(-1, 1)
        while tuple(self.location) not in locations:
            self.location = list(self.oldlocation)
            self.location[0]+= random.randint(-1, 1)
            self.location[1]+= random.randint(-1, 1)
        temp = numpy.subtract(self.location, self.oldlocation)
        temp = temp.tolist()   
        if  temp == [0,0]:
            return None
        elif temp in [[1,1], [1, -1],[-1, 1], [-1, -1]]:
                    self.nourishment -= 2
        else:
            self.nourishment -=1
        self.oldlocation = (tuple(self.location))

    def reproduce(self):     
        if  self.isReproducing == 1:
            self.isReproducing = 0
            blobs.append(Blob(0, 0, location=self.location))
    def die(self):
        if self.age >= 6:
            a = blobs.index(self)
            del(blobs[a])
            print("blob has died")



class Place:
    def __init__ (self, food, location):    
        self.location = location
        self.food = food

def initialize(foodmax, totalblobs, totalplaces, time):
    for x in range(0, totalplaces[0]+1):
        y=0
        for y in range(0, totalplaces[1]+1):
            places.append(Place(random.randint(0, int(foodmax)), (int(x), int(y))))
            y+=1
        x+=1
    for place in places:
        locations.append(place.location)
    for i in range(totalblobs):
        blobs.append(Blob(random.randint(0, 5), 0, location = list(random.choice(locations))))
        i+=1


def run(foodmax, totalblobs, totalplaces, time):
    initialize(foodmax, totalblobs, totalplaces, time)
    for i in range (time):
        for blob in blobs:
            print("blob at" + str(blob.location))
            blob.feed()
            blob.checkreproducing()
            blob.reproduce()
            blob.move()
            print("blob moved to " + str(blob.location))
            blob.age +=1
            blob.die()
        print(len(blobs))

run(10, 1 , (1,1), 10)