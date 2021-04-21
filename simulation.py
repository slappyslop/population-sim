import random
import numpy
import matplotlib
import matplotlib.pyplot as plt
places = []
blobs = []
locations = []
blobslist = []


class PopulationDied(Exception):
    pass


class Blob:
    def __init__(self, age, productivity, location=[0, 0]):
        self.age = age
        self.productivity = productivity
        self.location = location
        self.nourishment = 5
        self.isReproducing = 0
        self.oldlocation = tuple(location)

    def checkreproducing(self):
        if self.nourishment >= 8:
            self.isReproducing = 1
            self.nourishment -= 5

    def feed(self):
        for place in places:
            if place.location == tuple(self.location):
                if place.food > 0 and self.nourishment < 10:
                    place.food -= 1
                    self.nourishment = 10
                    return
                else:
                    return

    def move(self):
        self.location[0] += random.randint(-1, 1)
        self.location[1] += random.randint(-1, 1)
        while tuple(self.location) not in locations:
            self.location = list(self.oldlocation)
            self.location[0] += random.randint(-1, 1)
            self.location[1] += random.randint(-1, 1)
        temp = numpy.subtract(self.location, self.oldlocation)
        temp = temp.tolist()
        if temp == [0, 0]:
            return None
        elif temp in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            self.nourishment -= 2
        else:
            self.nourishment -= 1
        self.oldlocation = tuple(self.location)

    def die(self):
        a = blobs.index(self)
        if self.age >= 6 or self.nourishment <= 1:
            if len(blobs) > 1:
                del(blobs[a])
                print("blob has died")
            else:
                print("population died")
                raise PopulationDied


class Place:
    def __init__(self, food, location):
        self.location = location
        self.food = food


def initialize(foodmax, totalblobs, totalplaces, time):
    for x in range(0, totalplaces[0]+1):
        y = 0
        for y in range(0, totalplaces[1]+1):
            places.append(Place(random.randint(
                0, int(foodmax)), (int(x), int(y))))
            y += 1
        x += 1
    for place in places:
        locations.append(place.location)
    for i in range(totalblobs):
        blobs.append(Blob(random.randint(0, 5), 0,
                     location=list(random.choice(locations))))


def reproduce():
    for blob in blobs:
        if blob.isReproducing == 1:
            blob.isReproducing = 0
            if blob.location in locations:
                blobs.append(Blob(0, 0, location=blob.location))
            else:
                blobs.append(Blob(0, 0, list(random.choice(locations))))


def run(foodmax, totalblobs, totalplaces, time):
    initialize(foodmax, totalblobs, totalplaces, time)
    try:
        for i in range(time):
            for blob in blobs:
                print("blob at" + str(blob.location))
                blob.feed()
                blob.move()
                blob.checkreproducing()
                print("blob moved to " + str(blob.location))
                blob.age += 1
                blob.die()
                print("\n")
            reproduce()
            print(len(blobs))
            blobslist.append(len(blobs))
            print("\n\n")
            print(i)
        print("simulation done")
    except PopulationDied:
        pass


def plot():
    blobsarray = numpy.array(blobslist)
    plt.plot(blobsarray)
    plt.show()


run(10000, 1, (1, 1), 100)
plot()
