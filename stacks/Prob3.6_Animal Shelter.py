class AnimalShelter():
    def __init__(self) -> None:
        self.cats = []
        self.dogs = []

    def pushAnimal(self, animal, animal_type):
        if animal_type == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def popAnimal(self, animal_type=None):
        if animal_type == 'cat':
            if len(self.cats) == 0:
                return None
            else:
                poppedAnimal = self.cats.pop(0)
        
        elif animal_type == 'dog':
            if len(self.dogs) == 0:
                return None
            else:
                poppedAnimal = self.dogs.pop(0)

        else:
            if len(self.cats) == 0 and len(self.dogs) == 0:
                return None
            elif len(self.cats) == 0:
                poppedAnimal = self.dogs.pop(0)
            elif len(self.dogs) == 0:
                poppedAnimal = self.cats.pop(0)
            else:
                if len(self.cats) >= len(self.dogs):
                    poppedAnimal = self.cats.pop(0)
                else:
                    poppedAnimal = self.dogs.pop(0)

        return poppedAnimal
    
customQueue = AnimalShelter()
customQueue.pushAnimal('Cat1', 'cat')
customQueue.pushAnimal('Dog1', 'dog')
customQueue.pushAnimal('DOG2', 'dog')
customQueue.pushAnimal('cat2', 'cat')
customQueue.pushAnimal('dog3', 'dog')
customQueue.pushAnimal('CAT3', 'cat')
print(customQueue.popAnimal())
print(customQueue.popAnimal('dog'))
print(customQueue.popAnimal('cat'))         
