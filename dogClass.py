import random


class Dog:
    lastNames = [
        'Collins', 'Armstrong', 'Aldrin', 'Slayton', 'Shepard', 'Glenn', 'Grisom', 'Kranz', 'Kraft', 'Von Braun'
    ]

    firstNames = ['Michael', 'Neil', 'Buzz', 'Deac', 'Alan', 'John', 'Gus', 'Gene', 'Chris', 'Werner']

    names = list(zip(lastNames, firstNames))

    breeds = [
        'Rhodesian Ridgeback', 'German Shepard', 'Australian Shepard', 'Belgian Malinois', 'Shiba Inu', 'Bull Terrier'
    ]

    colors = ['Gold', 'Black', 'White', 'Brown', 'Mixed', 'Spotted']

    hospital = 'Serene Doge of Venice Hospital'

    def getCondition(self):
        if(random.randint(0, 1) == 1):
            return True
        else:
            return False

    def __init__(self, name='', weight=0, breed='', age=0, color='', condition=False):
        self.name = name or self.names[random.randint(0, (len(self.names) - 1))]
        self.weight = weight or random.randint(20, 60)
        self.breed = breed or self.breeds[random.randint(0, len(self.breeds)-1)]
        self.age = age or random.randint(0, 12)
        self.color = color or self.colors[random.randint(0, len(self.colors)-1)]
        self.condition = condition or self.getCondition()

    def printDog(self):
        print('In Care at ' + f'{self.hospital}')
        print('Name: ' + f'{self.name}')
        print('Weight: ' + f'{self.weight}')
        print('Breed: ' + self.breed)
        print('Age: ' + f'{self.age}')
        print('Color: ' + self.color)
        if(self.condition is True):
            print('Condition: Healthy')
        else:
            print('Condition: Sick')
