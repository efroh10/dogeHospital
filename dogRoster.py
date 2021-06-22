import random

class Dog:
    lastNames = ['Collins', 'Armstrong', 'Aldrin', 'Slayton', 'Shepard', 'Glenn', 'Grisom', 'Kranz', 'Kraft', 'Von Braun']
    firstNames = ['Michael', 'Neil', 'Buzz', 'Deac', 'Alan', 'John', 'Gus', 'Gene', 'Chris', 'Werner']
    names = list(zip(lastNames, firstNames))
    breeds = ['Rhodesian Ridgeback', 'German Shepard', 'Australian Shepard', 'Belgian Malinois', 'Shiba Inu', 'Bull Terrier']
    colors = ['Gold', 'Black', 'White', 'Brown', 'Mixed', 'Spotted']
    hospital = 'Serene Doge of Venice Hospital'


    def getCondition(self):
        if(random.randint(0, 1) == 1):
            return True
        else:
            return False

    def __init__(self, name = '', weight = 0, breed = '', age = 0, color = '', condition = False):
        self.name = name or self.names[random.randint(0, (len(self.names) - 1))]
        self.weight = weight or random.randint(20, 60)
        self.breed = breed or self.breeds[random.randint(0, len(self.breeds)-1)]
        self.age = age or random.randint(0,12)
        self.color = color or self.colors[random.randint(0, len(self.colors)-1)]
        self.condition = condition or self.getCondition()

    def printDog(self):
        print( 'In Care at ' + f'{self.hospital}')
        print('Name: ' + f'{self.name}')
        print('Weight: ' + f'{self.weight}')
        print('Breed: ' + self.breed)
        print('Age: ' + f'{self.age}')
        print('Color: ' + self.color)
        if(self.condition == True):
            print('Condition: Healthy')
        else:
            print('Condition: Sick')

patient1 = Dog()
patient2 = Dog()
patient3 = Dog()
patient4 = Dog()
patient5 = Dog()

currentPatients = [patient1, patient2, patient3, patient4, patient5]

currentRoster = [patient1.name, patient2.name, patient3.name, patient4.name, patient5.name]

def printCurrentRoster():
    counter = 1
    for x in currentRoster:
        print(f'{counter}' + ': ' + f'{x}')
        counter += 1

def customDog():
    name = input("Enter the dog's name")
    weight = int(input("Enter the dog's weight"))
    breed = input("Enter the dog's breed")
    age = input("Enter the dog's age")
    color = input("Enter the dog's color")
    patient = Dog(name, weight, breed, age, color, True)
    currentPatients.append(patient)
    currentRoster.append(patient.name)   

def doStuff():
    printCurrentRoster()
    action = int(input("Enter the number of the dog you'd like to know more about, or enter 0 to check in a new patient."))
    if(0 < action <= len(currentRoster)):
        currentPatients[action-1].printDog()
        doStuff()
    elif(action == 0):
        customDog()
        doStuff()
    else:
        print('Invalid Input')
        doStuff()

doStuff()