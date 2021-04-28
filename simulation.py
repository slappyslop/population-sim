import random
import numpy
import matplotlib
import matplotlib.pyplot as plt
from celluloid import Camera
import time
places = []
blobs = []
locations = []
blobslist = []
camera = Camera(plt.figure())
plt.rcParams["figure.figsize"] = (20,3)


class PopulationDied(Exception):
    pass #population died exception to end loop when only 1 is left


class Blob:
    def __init__(self, age, productivity, location=[0, 0]):
        self.age = age
        self.productivity = productivity
        self.location = location
        self.nourishment = 5 #basic health nutrition etc.
        self.isReproducing = 0 #flag for reproduction
        self.oldlocation = tuple(location)

    def checkreproducing(self): # checks if a blob can reproduce and sets flag
        if self.nourishment >= 8:
            self.isReproducing = 1
            self.nourishment -= 5

    def feed(self): #blob feeds, depleting food of place
        for place in places:
            if place.location == tuple(self.location):
                if place.food > 0 and self.nourishment < 10:
                    place.food -= 1
                    self.nourishment = 10
                    return
                else:
                    return

    def move(self): #moves randomly into a location right next to it
        self.location[0] += random.randint(-1, 1)
        self.location[1] += random.randint(-1, 1)
        while tuple(self.location) not in locations: # checks if location is illegal, if so, repeats move until it is not
            self.location = list(self.oldlocation)
            self.location[0] += random.randint(-1, 1)
            self.location[1] += random.randint(-1, 1)
        temp = numpy.subtract(self.location, self.oldlocation)
        temp = temp.tolist()
        if temp == [0, 0]:
            return None
        #elif temp in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            #self.nourishment -= 2
        else:
            self.nourishment -= 1
        self.oldlocation = tuple(self.location)

    def die(self): #kills blobs if starving or too old, unless only one is left, in which case 3 frames are created and code ends
        a = blobs.index(self)
        if self.age >= 20 or self.nourishment <= 1:
            if len(blobs) > 1:
                del(blobs[a])
                print("blob has died")
            else:
                print("population died")
                camera.snap()
                camera.snap()
                camera.snap()
                raise PopulationDied


class Place: #each position has two attritbutes, location, a coordinate tuple, and food quantity, an integer
    def __init__(self, food, location):
        self.location = location
        self.food = food


def initialize(foodmax, totalblobs, totalplaces,): #creates all possible positions according to total places arg, foodmax arg, and totalblobs arg. total places is a tuple with (xscale, yscale)
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


def reproduce(totalplaces):
    for blob in blobs:
        if blob.isReproducing == 1:
            blob.isReproducing = 0
            if tuple(blob.location) in locations:
                blobs.append(Blob(0, 0, location=blob.location))
            else:
                return


def run(foodmax, totalblobs, totalplaces, iterations, framedelay = 0, ):
    initialize(foodmax, totalblobs, totalplaces,)
    try:
        placesx = []
        placesy = []
        for place in places:
            placesx.append(place.location[0])
            placesy.append(place.location[1])
        for i in range(iterations):
            bloblocationsx = []
            bloblocationsy = []
            foodplacesx = []
            foodplacesy = []
            for blob in blobs:
                bloblocationsx.append(blob.location[0])
                bloblocationsy.append(blob.location[1])
                print("blob at" + str(blob.location))
                blob.feed()
                blob.move()
                blob.checkreproducing()
                print("blob moved to " + str(blob.location))
                blob.age += 1
                blob.die()
                print("\n")
            for place in places:
                if place.food > 0:
                    foodplacesx.append(place.location[0])
                    foodplacesy.append(place.location[1])
            plt.scatter(numpy.array(placesx), numpy.array(placesy), marker= ',', s = 2, c = '#dbdbb8')        
            plt.scatter(numpy.array(foodplacesx), numpy.array(foodplacesy), marker=",", s = 2 ,c = '#6eff6e')
            plt.scatter(numpy.array(bloblocationsx), numpy.array(bloblocationsy), marker = ",", s= 2, c= 'b')
            camera.snap()
            reproduce(totalplaces)
            print(len(blobs))
            blobslist.append(len(blobs))
            print("\n\n")
            time.sleep(framedelay)
            
        print("simulation done")
        writervideo = matplotlib.animation.FFMpegWriter(fps = 2)
        anim = camera.animate(blit=True)
        anim.save('run.mp4', writer=writervideo)
        print(blobslist)
    except PopulationDied:
        writervideo = matplotlib.animation.FFMpegWriter(fps = 2)
        anim = camera.animate(blit=True)
        anim.save('run.mp4', writer= writervideo)
        print(blobslist)
    except KeyboardInterrupt:
        writervideo = matplotlib.animation.FFMpegWriter(fps = 2)
        anim = camera.animate(blit=True)
        anim.save('run.mp4', writer= writervideo)
        print(blobslist)


def plot():
    blobsarray = numpy.array(blobslist)
    plt.plot(blobsarray)
    plt.show()

def animate():  
    pass

run(1, 10, (100,100), 1000)
plot()
