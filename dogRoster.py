from dogClass import Dog

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
    action = int(input(
        "Enter the number of the dog you'd like to know more about, or enter 0 to check in a new patient."
    ))
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
