class Animal:
    def __init__(self, type, order=None):
        self.order = order
        self.type = type

    def is_dog(self):
        return self.type == "Dog"

    def is_cat(self):
        return self.type == "Cat"

    def is_older_than(self, animal):
        return self.order > animal.order

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order_couter = 0

    def enqueue(self, animal):
        animal.order = self.order_couter
        self.order_couter +=1

        if animal.is_dog():
            self.dogs.append()
        elif animal.is_cat():
            self.cats.append()

    def dequeue_any(self):
        if not self.dogs:
            return self.dequeue_cat
        elif not self.cats:
            return self.dequeue_dog
        else:
            if self.dogs[-1].is_older_than(self.cats[-1]):
                return self.dequeue_dog
            else:
                return self.dequeue_cat