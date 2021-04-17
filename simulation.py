import random
import csv
import numpy
import pandas as pd



startingPopulation = 300
#infantMortality = 25
productivity=5
#disasterChance = 10
food = 0
fertilityx = 18
fertilityy = 40
fertilitychance = 20
people = []
year =1 
foodvalues = []
peoplevalues = []




class Person:
    def __init__(self, age):
        self.age = age
        self.sex = random.randint(0,1)


def harvest():
    ablepeople = 0 
    for person in people:
        if person.age>8:
            ablepeople +=1
    print(ablepeople, "able people")
    
    global food

    food +=(ablepeople*productivity)
    print(food, "after hravesting")
    if food<len(people):
        del people[0:int(len(people)-food)]
        food = 0
    else:
        food = food -len(people)

def reproduce():
    for person in people:
        if person.sex == 1:
            if fertilityx<=person.age and person.age<= fertilityy:
                if random.randint(1, (100/fertilitychance)) == 1:
                    people.append(Person(0))
        else:
            continue


def beginSim():
    for i in range(startingPopulation):
        people.append(Person(random.randint(18,50)))

def runYear():
    harvest()
    print(food, "food after eating")
    reproduce()
    print(len(people), "after reproduction")
    for person in people:
        if person.age > 80:
            people.remove(person)
        else:
            person.age +=1
    print(len(people), "after old age")


beginSim()
while len(people)<100000 and len(people) > 1:
    print(year , " year")
    runYear()
    year +=1
    peoplevalues.append(len(people))
    foodvalues.append(food)

