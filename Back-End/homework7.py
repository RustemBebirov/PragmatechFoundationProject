from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def run(self):
        pass

    
    @abstractmethod   
    def stop(self):
        pass


class Dog(Animal):

    def run(self):
        print("It qacmaga basladi")
    
    def stop(self):
        print("IT dayandi")

class Cat(Animal):

    def run(self):
        print("pisik qacmaga basladi")

    def stop(self):
        print("pisik dayandi")


dog1=Dog()
dog1.run()
dog1.stop()
cat1=Cat()
cat1.run()
cat1.stop()